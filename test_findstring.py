from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent("Ad")

# To test_nodigit fails because it contains numeric character while the test_ispresent passes

def test_nodigit():
    assert findstring.nodigit("N7")

    """""To rectify it you
- Write the test cases with some functionality in mind
- write the code in accordance to the test cases ensuring that they pass
- Refactor code incase of failure"""