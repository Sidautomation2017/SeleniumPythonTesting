# PyTest file always start with test_ or ends with _test
# PyTestmethod should start with test
# Every code should be wrapped inside method in PyTest
# every method is a test in PyTest
import pytest


def test_firstProgram():
    print("First program with PyTest")


@pytest.mark.smoke
def test_secondProgram():
    print("Second program with PyTest")
