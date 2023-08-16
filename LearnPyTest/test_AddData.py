import pytest


def testLogin():
    print("Login Successfull")

def testLogOff():
    print("LogOff Successfull")

@pytest.mark.xfail
def testAirthmetic():
    assert 2+3==4