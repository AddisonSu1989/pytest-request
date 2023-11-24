import pytest
from testcases.conftest import api_data_addison


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data_addison.get(testcase_name)