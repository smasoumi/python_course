import pytest
from mathlib import *


# skip one test for a desired reason
@pytest.mark.skip(reason='do not run test for now')
def test_sum():
    res = sum1(5, 2)
    assert res == 7


def test_mul():
    res = mul1(5, 2)
    assert res == 10
