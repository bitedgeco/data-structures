from hash import Hash

WORDS = '/mnt/c/py401d/words'

def test_set_and_get():
    """put something in the hash table then make sure its there"""
    table = Hash(10)
    table.set('blue', 8)
    assert table.get('blue') == 8

def test_fnv_hash():
    """Test fnv hash with a set and get method."""
    table = Hash(10)
    table.set_fnv('test', 'test2')
    assert table.get_fnv('test') == 'test2'

def test_words_additive():
    """Test from a word list additive."""
    table = Hash(1000)
    for word in open(WORDS):
        table.set(word, word)
    for word in open(WORDS):
        assert table.get(word) == word

def test_words_fnv():
    """Test fnv against a word list."""
    table = Hash(2000)
    for word in open(WORDS):
        table.set_fnv(word, word)
    for word in open(WORDS):
        assert table.get_fnv(word)

def test_othash():
    """Test othash."""
    table = Hash(10)
    table.otset('blue', 10)
    assert table.otget('blue') == 10