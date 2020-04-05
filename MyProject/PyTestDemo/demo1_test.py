import pytest


@pytest.mark.xfail
def test_firstDemo():
    msg = "Hi"
    assert msg == "Hi", "String mismatch"


@pytest.mark.smoke
@pytest.mark.skip
def test_secondDemo():
    a = 2
    b = 5
    assert a + b == 7, "Sum is not correct"
