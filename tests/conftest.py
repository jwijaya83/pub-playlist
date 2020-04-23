import pytest
from tests.api.api_helper import ApiHelper


def pytest_addoption(parser):
    parser.addoption("--graphql_url", action="store", default="http://localhost:3000/graphql")


@pytest.fixture(scope='class')
def api_communicator(request):
    return ApiHelper(request.config.getoption('--graphql_url'))
