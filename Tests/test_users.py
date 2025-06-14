import requests
import json
import jsonpath


"""
测试用例：
1. 获取用户信息
2. 创建用户
3. 删除用户
"""


#定义接口的基础域名，后续接口路径会拼接在它后面，形成完整请求URL，这里是测试用的在线接口服务地址
baseUrl = "https://reqres.in/"
#接口的身份验证密钥(示例值,实际接口按规则使用)，用于请求头标识身份，部分接口需要通过此校验权限
API_KEY='reqres-free-v1'

#通用请求头配置
headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}
def test_fetch_user() :


    #定义具体接口路径，拼接在baseUrl后面就是完整URL(https://reqres.in/api/users/2),用于获取ID为2的用户信息。
    path = "api/users/2"

     #是requests库的Response对象。
    response = requests.get(url=baseUrl+path, headers=headers)  # 添加请求头
   
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2


def test_create_delete_user() :
    with open("TestData/user.json", "r") as file:
        inputData=json.loads(file.read())
    path = "api/users"

    # 创建用户（添加请求头）
    response = requests.post(
        url=baseUrl + path,
        json=inputData,
        headers=headers  # 添加请求头
    )
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == inputData["name"]
    
    # 删除用户（添加请求头）
    user_id = jsonpath.jsonpath(responseJson, '$.id')[0]
    delete_response = requests.delete(
        url=baseUrl + path + '/' + str(user_id),
        headers=headers  # 添加请求头
    )
    assert delete_response.status_code == 204

  