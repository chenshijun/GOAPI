import pytest
from pytest_testconfig import load_ini, config
from util.Properties import Properties
import os

currentPath = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default='qa',
        help="options: qa or dev or prod",
    )


@pytest.fixture(autouse=True, scope="session")
def env(request):
    print("****************当前接口运行环境为：【{}】****************".format(request.config.getoption("--env")))
    running_env = request.config.getoption("--env")
    config.update({"running_env": running_env})
    path = os.path.join(currentPath, "config", running_env)
    for root, dirs, files in os.walk(path):
        for file in files:
            if '.ini' in file:
                load_ini(ini_file=os.path.join(path, file), encoding='utf8')
    props = Properties("./report/environment.properties")
    props.put("test_environment", running_env)
    return running_env
