def test_insertion_sort_small():
    from insertion_sort import insertion_sort
    assert insertion_sort([10,9,8,7,6,5,4,3,2,1,0]) == [0,1,2,3,4,5,6,7,8,9,10]

def test_insertion_ordered():
    from insertion_sort import insertion_sort
    assert insertion_sort([0,1,2,3,4,5,6]) == [0,1,2,3,4,5,6,]

def test_insertion_on_empty():
    """Test insertion sort on empty list."""
    from insertion_sort import insertion_sort
    assert insertion_sort([]) == []


def test_insertion_sort_on_one():
    """Test insertion sort on list of one."""
    from insertion_sort import insertion_sort
    assert insertion_sort([1]) == [1]