from radix import radix


def test_empty_list():
    '''test radix on simple list'''
    assert radix([]) == []


def test_single_item():
    '''test radix on simple list'''
    assert radix([3]) == [3]


def test_simple_list():
    '''test radix on simple list'''
    data = [3, 8, 5]
    radix(data)
    assert data == [3, 5, 8]


def test_list_with_zero():
    '''test radix on a list with 0'''
    data = [0, 1000, 2]
    radix(data)
    assert data == [0, 2, 1000]


def test_list_with_duplicates():
    '''test radix on larger list'''
    data = [19, 20, 20, 20, 21]
    radix(data)
    assert data == [19, 20, 20, 20, 21]


def test_list_with_powers():
    '''test radix on list with powers'''
    data = [100, 1000, 10, 10000, 1]
    radix(data)
    assert data == [1, 10, 100, 1000, 10000]


def test_list_with_all_kinds_of_stuff():
    '''test radix on list with all the things'''
    data = [37, 36, 34, 24, 20, 21, 128, 122, 116, 112, 200, 100]
    radix(data)
    assert data == [20, 21, 24, 34, 36, 37, 100, 112, 116, 122, 128, 200]
