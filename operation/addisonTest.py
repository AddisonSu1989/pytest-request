from core.result_base import ResultBase
from api.addisonTest import addisonTest
from common.logger import logger

def get_template():
    """
    获取全部用户信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = addisonTest.template()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["users"])
    result.msg = res.json()["users"]
    result.response = res
    return result

def register(username):
    """
    获取全部用户信息
    :return: 自定义的关键字返回结果 result
    """
    json_data = {
        "userName": username
    }
    header = {
        "Content-Type": "application/json"
    }
    result = ResultBase()
    res = addisonTest.registerUser(json=json_data,headers=header)
    result.success = False
    if res.json()["code"] == 10001:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["userName"])
    result.msg = res.json()["userName"]
    result.response = res
    return result

