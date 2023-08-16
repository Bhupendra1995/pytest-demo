import pytest

#autouse = True means this fixture is applicable on all and no need to give the argument as fixture name

@pytest.fixture(scope="session",autouse=True)
def SetUpANDTearDown(GetBrowser):
    if GetBrowser == "chrome":
        print("Launch Chrome")
    elif GetBrowser == "FF":
        print("Launch Firefox")
    else:
        print("enter valid browser")
    print("Search Item")
    print("Choose Item")
    yield
    print("LogOff")
    print("close Browser")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def GetBrowser(request):
    _browser =  request.config.getoption("--browser", default="chrome")
    return  _browser


