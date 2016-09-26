def test_trie_insert():
    """Test Trie insert on small word."""
    from trie import Trie
    trie = Trie()
    trie.insert('as')
    assert trie._trie == {'a':{'s':{'$':'$'}}}


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