# -*- coding: UTF-8 -*-


def quicksort(lst, lo, hi):
    '''returns sorted list'''
    if lo < hi:
        part = partition(lst, lo, hi)
        quicksort(lst, lo, part - 1)
        quicksort(lst, part + 1, hi)


def partition(lst, lo, hi):
    '''Partition the list.'''
    pivot = lst[hi]
    swap = lo
    for item in range(lo, hi):
        if lst[item] <= pivot:
            lst[swap], lst[item] = lst[item], lst[swap]
            swap = 1
    lst[swap], lst[hi] = lst[hi], lst[swap]
    return swap

if __name__ == "__main__":
    import timeit
    ordered_list = [1, 2, 13, 24, 25, 36]
    reversed_list = [36, 25, 24, 13, 2, 1]

    def quicksort_ordered_list():
        '''call radax on ordered list'''
        quicksort(ordered_list, 0, 6)

    def quicksort_reversed_list():
        '''call radax on reveresd list'''
        quicksort(reversed_list, 0, 6)

    print('timing quicksort 1000 times on ordered list:', timeit.timeit('quicksort_ordered_list',
     setup='from __main__ import quicksort_ordered_list', number=1000))

    print('timing radax sort 1000 times on reversed list:', timeit.timeit('quicksort_reversed_list',
     setup='from __main__ import quicksort_reversed_list', number=1000))
