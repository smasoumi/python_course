import sys

import pytest
from mathlib import *


# skip one test for a desired reason
@pytest.mark.skip(reason='do not run test for now')
def test_sum():
    res = sum1(5, 2)
    assert res == 7


@pytest.mark.skipif(sys.version_info < (3, 9), reason='requires Python 3.9 or higher')
def test_mul():
    res = mul1(5, 2)
    assert res == 10


# test a method with different parameters at once
@pytest.mark.parametrize('input1, input2, output', [(3, 4, 7), (10, 15, 25), (-1, 5, 4)])
def test_parametrized_sum(input1, input2, output):
    assert sum1(input1, input2) == output
