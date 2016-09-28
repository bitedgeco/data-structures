# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from quicksort import quicksort


def test_quicksort():
    data = [4, 8, 33, 6, 2, 99]
    assert quicksort(data) == [2, 4, 6, 8, 33, 99]


def test_quicksort_empyy():
    data = []
    assert quicksort(data) == []


def test_quicksort_one_val():
    data = [4]
    assert quicksort(data) == [4]


def test_quicksort_two_vals():
    data = [6, 5]
    assert quicksort(data) == [5, 6]
