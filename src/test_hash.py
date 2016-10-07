from hash import Hash


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