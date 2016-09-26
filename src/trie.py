
class Trie(object):
    """Python Trie"""

    def __init__(self, ):
        """Initialize trie."""
        self._trie = {}

    def insert(self, token):
        start = self._trie 
        for char in token:
            start = start.setdefault(char, {})
        start['$'] = '$'
    
    def contains(self, token):
        start = self._trie
        for char in token:
            try:
                start = start[char]
            except KeyError:
                return False
        try:
            start['$'] = '$'
            return True
        except KeyError:
            return False
