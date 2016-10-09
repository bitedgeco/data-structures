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

    def _hash_fnv(self, key):
        """Use FNV to hash key."""
        hash = 2166136261
        for char in key:
            hash = (hash * 16777619) ^ ord(char)
        return hash % self.size
    
    def set_fnv(self, key, value):
        """Set key value using fnv."""
        slot = self._hash_fnv(key)
        self.table[slot].append((key, value))
        
    def get_fnv(self, key):
        """Get value from key using fnv hash."""
        hashed = self._hash_fnv(key)
        for tup in self.table[hashed]:
            if tup[0] == key:
                return tup[1]
    
    def _hash_ot(self, key):
        """Hashing using one at a time method."""
        hash = 0
        for char in key:
            hash += ord(char)
            hash +=  (hash << 10)
            hash ^= (hash >> 6)
        hash +=  (hash << 3)  
        hash ^= (hash >> 11)
        hash += (hash << 15 )
        return hash % self.size

    def otset(self, key, value):
        """Set key value using one at a time hash."""
        slot = self._hash_ot(key)
        self.table[slot].append((key, value))
        
    def otget(self, key):
        """Get value from an ot hashed table."""
        hashed = self._hash_ot(key)
        for tup in self.table[hashed]:
            if tup[0] == key:
                return tup[1]



