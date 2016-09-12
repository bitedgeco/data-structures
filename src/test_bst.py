# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bst import BST
import pytest


# def test_insert_val_exists():
#     """Test cannot insert val that already exists."""
#     bst = BST()
#     with pytest.raises(ValueError) as message:
#         bst.insert(10)
#     assert "That value already exists." in str(message)


def test_insert_from_empty():
    """Test can insert into empty binary search tree."""
    bst = BST()
    bst.insert(1)
    assert bst.root.val == 1


def test_insert_correct_place_start_empty():
    """Test insert into correct place from empty bst."""
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    assert bst.root.right.val == 2


def test_insert_from_existing(bst_test_case):
    """Test insert into correct position bst with existing values."""
    bst_test_case.insert(3)
    assert bst_test_case.root.left.left.val == 3


# def test_insert_at_start_from_existing(bst_test_case):
#     """Test insert at correct position of bst that has existing values."""
#     bst_test_case.insert(22)
#     assert
#
#
# def test_insert_at_end_from_existing(bst_test_case):
#     """Test insert at correct position of bst that has existing values."""
#     bst_test_case.insert(88)
#     assert
