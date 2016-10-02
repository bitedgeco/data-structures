 # -*- coding: UTF-8 -*-
def quicksort(lst, lo, hi):
    '''returns sorted list'''
    if lo  < hi:
        part = partition(lst, lo, hi)
        quicksort(lst, lo, part -1)
        quicksort(lst, part +1, hi)

def partition(lst, lo, hi):
    """Partition the list."""
    pivot = lst[hi]
    swap = lo
    for item in range(lo, hi):
        if lst[item] <= pivot:
            lst[swap], lst[item] = lst[item], lst[swap]
            swap += 1
    lst[swap], lst[hi] = lst[hi], lst[swap]
    return swap