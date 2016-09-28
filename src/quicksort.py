def quicksort(lst):
    '''returns sorted list'''
    piv = len(lst) // 2
    small_sub_list = []
    big_sub_list = []
    for val in lst:
        if val < lst[piv]:
            small_sub_list.append(val)
        else:
            big_sub_list.append(val)
    if len(small_sub_list) > 1:
        if len(small_sub_list) == 2:
            if small_sub_list[1] > small_sub_list[0]:
                small_sub_list[1], small_sub_list[0] = small_sub_list[0], small_sub_list[1]
        else:
            quicksort(small_sub_list)
    if len(big_sub_list) > 1:
        if len(big_sub_list) == 2:
            if big_sub_list[1] < big_sub_list[0]:
                big_sub_list[1], big_sub_list[0] = big_sub_list[0], big_sub_list[1]
        else:
            quicksort(big_sub_list)
    small_sub_list.extend(big_sub_list)
    # import pdb; pdb.set_trace()

    return small_sub_list


# if __name__ == ‘__main__’:
