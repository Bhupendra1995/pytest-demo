import pytest

def testLogin():
    print("Login Successfull")

@pytest.mark.skip
def testLogOff():
    print("LogOff Successfull")

def testAirthmetic():
    assert 2+2==4