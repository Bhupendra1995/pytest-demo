import pytest

@pytest.mark.parametrize("a, b, final",[(2,4,6),(4,8,13),(3,10,13)])
def testLogin(a,b,final):
    assert a+b == final

