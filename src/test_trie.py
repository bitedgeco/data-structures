def test_trie_insert():
    """Test Trie insert on small word."""
    from trie import Trie
    trie = Trie()
    trie.insert('as')
    assert trie._trie == {'a': {'s': {'$': '$'}}}


def test_simple_contains():
    """Test simple contains."""
    from trie import Trie
    trie = Trie()
    trie.insert('as')
    assert trie.contains('as')


def test_simple_contains_false():
    """Test simple contains is false."""
    from trie import Trie
    trie = Trie()
    trie.insert('as')
    assert trie.contains('f') is False


def test_trie_traversal():
    """Test a simple trie for traversal."""
    from trie import Trie
    trie = Trie()
    trie.insert('for')
    trie.insert('forest')
    trie.insert('fun')
    assert list(trie.traversal(trie._trie)) == ['for', 'forest', 'fun']


def test_trie_single():
    """Test trie with a single insert."""
    from trie import Trie
    trie = Trie()
    trie.insert('token')
    assert list(trie.traversal(trie._trie)) == ['token']


def test_trie_empty():
    """Test trie with an empty trie."""
    from trie import Trie
    trie = Trie()
    assert list(trie.traversal(trie._trie)) == []


def test_trie_big_list():
    """Test trie on a bigger list."""
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('ab')
    trie.insert('abs')
    trie.insert('age')
    trie.insert('ages')
    trie.insert('bag')
    trie.insert('baggage')
    trie.insert('bags')
    assert 'age' in list(trie.traversal(trie._trie))


def test_trie_big_list2():
    """Test trie on a bigger list part 2."""
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('ab')
    trie.insert('abs')
    trie.insert('age')
    trie.insert('ages')
    trie.insert('bag')
    trie.insert('baggage')
    trie.insert('bags')
    assert 'baggage' in list(trie.traversal(trie._trie))

def test_len_big_list():
    """Test trie on a bigger list part 2."""
    from trie import Trie
    trie = Trie()
    trie.insert('a')
    trie.insert('ab')
    trie.insert('abs')
    trie.insert('age')
    trie.insert('ages')
    trie.insert('bag')
    trie.insert('baggage')
    trie.insert('bags')
    assert len(list(trie.traversal(trie._trie))) == 8
