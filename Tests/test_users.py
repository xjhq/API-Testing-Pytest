import os
import json
import requests
import jsonpath
import allure
import pytest

@allure.epic("用户管理系统")
@allure.feature("用户API测试")
class TestUsersAPI:
    """用户管理模块CRUD测试"""

    # 类级别配置
    base_url = "https://reqres.in/"
    api_key = "reqres-free-v1"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    @property
    def test_data_path(self):
        """动态获取测试数据路径"""
        return os.path.join(
            os.path.dirname(__file__), 
            "../TestData/user.json"
        )

    @allure.story("获取用户信息")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke")
    def test_fetch_user(self):
        """测试获取指定用户信息"""
        with allure.step("准备请求数据"):
            endpoint = "api/users/2"
            url = f"{self.base_url}{endpoint}"
            allure.attach(url, "请求URL", allure.attachment_type.URI_LIST)

        with allure.step("发送GET请求"):
            response = requests.get(url=url, headers=self.headers)
            allure.attach(
                json.dumps(dict(response.headers), indent=2),
                "响应头",
                allure.attachment_type.JSON
            )

        with allure.step("验证响应"):
            response_data = response.json()
            allure.attach(
                json.dumps(response_data, indent=2),
                "完整响应",
                allure.attachment_type.JSON
            )
            
            assert response.status_code == 200
            assert jsonpath.jsonpath(response_data, '$.data.first_name')[0] == 'Janet'
            assert jsonpath.jsonpath(response_data, '$.data.id')[0] == 2

    @allure.story("用户生命周期管理")
    @allure.tag("regression")
    def test_create_delete_user(self):
        """测试创建和删除用户全流程"""
        with allure.step("加载测试数据"):
            with open(self.test_data_path, "r") as f:
                user_data = json.load(f)
                allure.attach(
                    json.dumps(user_data, indent=2),
                    "测试数据",
                    allure.attachment_type.JSON
                )

        with allure.step("创建用户"):
            endpoint = "api/users"
            response = requests.post(
                url=f"{self.base_url}{endpoint}",
                json=user_data,
                headers=self.headers
            )
            response_data = response.json()
            allure.attach(
                json.dumps(response_data, indent=2),
                "创建响应",
                allure.attachment_type.JSON
            )
            
            assert response.status_code == 201
            assert response_data["name"] == user_data["name"]
            user_id = response_data["id"]

        with allure.step("删除用户"):
            delete_response = requests.delete(
                url=f"{self.base_url}{endpoint}/{user_id}",
                headers=self.headers
            )
            assert delete_response.status_code == 204

  