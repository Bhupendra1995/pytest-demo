import pytest


def test_add_Item():
    print("Item added Successfully")

@pytest.mark.xfail
def test_Remove_Item():
    print("Item Removed Successfully")