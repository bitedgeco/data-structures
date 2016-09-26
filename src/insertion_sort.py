
def insertion_sort(lst):
    """Insertion Sort method."""
    if len(lst) <= 0:
        return lst
    
    for item in lst[1:]:
        cur_idx = lst.index(item)
        left_idx = cur_idx - 1
        while lst[left_idx] > item and left_idx >= 0:
            lst[left_idx + 1] = lst[left_idx]
            left_idx = left_idx -1
        lst[left_idx + 1] = item
    return lst 
