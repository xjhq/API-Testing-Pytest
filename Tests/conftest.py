#pytest全局配置
import pytest
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """处理测试失败时自动附加日志"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        allure.attach(
            "失败截图或日志", 
            name="失败详情",
            attachment_type=allure.attachment_type.TEXT
        )