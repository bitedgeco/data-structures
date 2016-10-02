# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from quicksort import quicksort
import pytest

TEST_CASES =[
    ([10,9,8,7,6,4], [4,6,7,8,9,10]),
    ([0,0,0,0], [0,0,0,0]),
    ([1,2,3,4,5,6], [1,2,3,4,5,6]),
    ([8,23,6,23,432,53], [6,8,23,23,53,432])
]
def test_quicksort():
    # import pdb; pdb.set_trace()
    data = [4, 8, 33, 6, 2, 99]
    quicksort(data, 0, 5) 
    assert data == [2, 4, 6, 8, 33, 99]


def test_quicksort_empyy():
    data = []
    quicksort(data, 0, 0) 
    assert data == []


def test_quicksort_one_val():
    data = [4]
    quicksort(data, 0, 0)
    assert data  == [4]


def test_quicksort_two_vals():
    data = [6, 5]
    quicksort(data, 0, 1) 
    assert data == [5, 6]

@pytest.mark.parametrize("input, result", TEST_CASES)
def test_with_params(input,result):
    """Test quicksort with paramerterize."""
    data = input
    quicksort(data, 0, len(data)-1)
    assert data == result
