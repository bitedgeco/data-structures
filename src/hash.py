from random import randint


class Hash(object):
    """a hash class"""
    def __init__(self, size):
        self.table = []
        self.size = size
        for i in range(0, size):
            self.table.append([])

    def _hash(self, key):
        """hash the key provided"""
        hash = len(key) * randint(0, 9) % self.size
        return hash

    def get(self, key):
        """takes key returns assoseated value"""
        for item in self.table:
            for tup in item:
                if tup[0] == key:
                    return tup[1]

    def set(self, key, val):
        """takes key and value and stores them in the table"""
        pair = (key, val)
        slot = self._hash(key)
        self.table[slot].append(pair)
