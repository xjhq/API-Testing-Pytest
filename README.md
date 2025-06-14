# Pytest-使用python`requests`进行API测试
 
[![API Tests with Pytest](https://github.com/ghoshasish99/API-Testing-Pytest/actions/workflows/pytest.yml/badge.svg)](https://github.com/ghoshasish99/API-Testing-Pytest/actions/workflows/pytest.yml)

#### Python是一个成熟的全功能Python测试框架，可以帮助你编写和运行Python测试。

#### `requests`模块允许您使用Python进行HTTP请求。

## 入门指南
要下载并安装`pytest`,请在终端运行以下命令：pip install pytest

要下载并安装`requests`,请在终端运行以下命令：pip install requests

为确保在ci环境中一次性解决所有依赖问题，请将他们添加到requirements.txt文件中。

然后运行以下命令：pip install -r requirements.txt

默认情况下，pytest仅识别以test_开头或以_test结尾的文件作为测试文件
pytest要求测试方法名称以test开头。即使我们明确要求运行其他方法，这些方法也会被忽略。
以下是一个测试示例：

```python
def test_fetch_user() :
    path = "api/users/2"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2

```
## 运行测试

如果您的测试包含在文件夹`Tests`中,请运行以下命令：`pytest Tests` 

要生成XML格式的测试结果，请运行以下命令：`pytest Tests --junitxml="result.xml"`
有关Pytest的更多信息，请访问这里(https://docs.pytest.org/en/stable/)