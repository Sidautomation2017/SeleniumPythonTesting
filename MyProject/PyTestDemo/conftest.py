import pytest


@pytest.fixture(scope="class")
def setup():
    print("Launch test ")
    yield
    print("End test")


@pytest.fixture()
def dataLoad():
    print("data method is called")
    tup = ["Sid", "Tondare", "AutomationTesting"]
    return tup


@pytest.fixture(params=[("chrome", "Sid"), ("firefox", "Tondare"), ("edge", "Automation")])
def crossBrowser(request):
    return request.param
