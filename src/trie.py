
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
            start['$'] == '$'
            return True
        except KeyError:
            return False

    def traversal(self, start=None):
        """Travese the tree using depth first and yeild words."""
        path = [start]
        word = ['']
        while path:
            current_dict = path.pop()
            current_word = word.pop()
            for key in list(current_dict.keys()):
                if key == '$':
                    yield current_word
                else:
                    path.append(current_dict[key])
                    word.append(current_word + key)
