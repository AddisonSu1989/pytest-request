import pytest
import allure
from operation.addisonTest import register
from testcases.conftest import api_data_addison
from common.logger import logger

@allure.step("步骤1 ：注册成功")
def step_1():
    logger.info("步骤1 ==>> 注册成功")

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("注册接口")
class TestTemplate():

    @allure.story("用例--注册成功接口")
    @allure.description("注册成功接口")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("user_name,except_result, except_code, except_msg",
                             api_data_addison["test_register_success"])
    def test_register_success(self,user_name,except_result, except_code, except_msg):
        step_1()
        ## 请求
        result = register(user_name)
        ## 断言
        assert result.response.status_code == 200
        assert result.success == except_result

        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--注册失败接口")
    @allure.description("注册失败接口")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("user_name,except_result, except_code, except_msg",
                             api_data_addison["test_register_failed"])
    def test_register_failed(self,user_name,except_result, except_code, except_msg):
        step_1()
        ## 请求
        result = register(user_name)
        ## 断言
        assert result.response.status_code == 200
        assert result.success == except_result

        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register.py"])