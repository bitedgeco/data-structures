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
        hash = 0
        for char in key:
            hash += ord(char)
        hash = hash % self.size
        return hash

    def get(self, key):
        """takes key returns assoseated value"""
        hashed = self._hash(key)
        for tup in self.table[hashed]:
            if tup[0] == key:
                return tup[1]

    def set(self, key, val):
        """takes key and value and stores them in the table"""
        pair = (key, val)
        slot = self._hash(key)
        self.table[slot].append(pair)

    # def _hash_fnv(self, key):
    #     """Use FNV to hash key."""
    #     hash = 2166136261
    #     for char in key:
    #         hash = (hash * 16777619) ^ ord(char)
    #     return hash % self.size
    