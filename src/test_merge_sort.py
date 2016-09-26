
def test_merge_sort_on_emtpy():
    """Test merge sort on empty."""
    from merge_sort import merge_sort
    lst = []
    merge_sort([]) == []
    assert lst == []
    
def test_merge_sort_on_one():
    """Test mrege sort on one."""
    from merge_sort import merge_sort
    lst = [1]
    merge_sort(lst)
    assert lst == [1]

def test_mege_sort_on_small():
    """Test merge sort on small."""
    from merge_sort import merge_sort
    lst = [1,10,3,8,4,5]
    merge_sort(lst)
    assert lst == [1,3,4,5,8,10]
