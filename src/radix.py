# -*- coding: utf-8 -*-


def radix(input):
    '''input a list, return the list ordered lowest to highest'''
    if len(input) < 2:
        return input

    maxlength = False
    place = 1

    while not maxlength:
        maxlength = True
        buckets = [[], [], [], [], [], [], [], [], [], []]

        for val in input:
            tmp = val // place
            buckets[tmp % 10].append(val)
            if maxlength and tmp > 0:
                maxlength = False

        index = 0
        for b in range(10):
            buck = buckets[b]
            for val in buck:
                input[index] = val
                index += 1
        place = place * 10


if __name__ == "__main__":
    import timeit
    ordered_list = [1, 2, 13, 24, 25, 36]
    reversed_list = [36, 25, 24, 13, 2, 1]

    def radix_ordered_list():
        '''call radax on ordered list'''
        radix(ordered_list)

    def radix_reversed_list():
        '''call radax on reveresd list'''
        radix(reversed_list)

    print('timing radax sort 1000 times on ordered list:', timeit.timeit('radix_ordered_list',
        setup='from __main__ import radix_ordered_list', number=1000))

    print('timing radax sort 1000 times on reversed list:', timeit.timeit('radix_reversed_list',
        setup='from __main__ import radix_reversed_list', number=1000))
