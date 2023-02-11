import addiction
import pytest


def test_add():
    assert True  # This means that all the test functions should return True for the test to pass
    assert addiction.add(5, 7) == 12


def test_sub():
    assert addiction.sub(5, 7) == -2

    # To run a single file, you add double colon at the end of file name while compiling
