class HashDict:
    '''
    This is a hash dictionary, aka. (key, value) tuples, that uses hashing to store the tuples in an array. The key must be a string, but the value can be anything.

    Abstraction function
	abs(c) = {k -> v | (k,v) in self._data; (k,v) /= None; (k,v) /= "TOMB, TOMB"}

    DTI:
    1. curSize is updated
    2. mSize is updated
    3. curSize < mSize, so data is never full
    4. nTomb is updated
    '''

    def __init__(self):
        self._mSize = 4
        self._curSize = 0
        self._maxLoadFactor = 0.5
        self._data = [None] * 4
        self._nTombs = 0
        self._tomb = ("TOMB", "TOMB")
        
    def __str__(self):
        out = ""
        for i in range(self._mSize):
            datum = ""
            if self._data[i] is not None:
                k, v = self._data[i]
                datum = k + " -> " + str(v)
            out += str(i) + "\t" + datum + "\n"

        return out

    def add(self, key, val):
        '''
        Adds (key, val) tuple into the dictionary

        :type key: string
        '''
        i = self._find(key)
        if not self._hasKey(key, i):
            self._curSize += 1
        if self._isTomb(i):
            self._nTombs -= 1
        self._data[i] = (key, val)

        if self._isAtMaxLoadFactor():
            self._doubleSize()
        elif self._tooManyTombs():
            self._clearTombs()

    def lookUp(self, key):
        '''
        Returns the value associated with *key* if it's in the dictionary, return None if not

        :type key: string
        :rtype any
        '''
        i = self._find(key)
        if not self._hasKey(key, i):
            return None
        else:
        	return self._data[i][1]

    def delete(self, key):
        '''
        Deletes the (key, value) pair of *key* and places a tomb on the spot
        Return True if successful and False if not (key not found)

        :type key: string
        :rtype bool
        '''
        i = self._find(key)
        if not self._hasKey(key, i):
            return False
        else:
            self._data[i] = self._tomb
            self._curSize -= 1
            self._nTombs += 1
            return True
 
    def size(self):
        return self._curSize

    def _h1(self, key):
        return hash(key)

    def _h2(self, key):
        total = 0
        for char in key:
            total += hash(char)
        return total

    def _find(self, key):
        '''
        The helper that powers all public functions.
        It takes a key and return the index in the array of the (key, value) tuple if found, and returns the index of the next available empty slot or tomb if not found.
        Pre: the internal array is not full.

        :type key: string
        :rtype int
        '''
        d = self._h1(key) % self._mSize
        prev = None

        if self._data[d] is None or self._hasKey(key, d):
            return d
        if self._isTomb(d):
            prev = d

        n = 1 + 2 * self._h2(key) % (self._mSize // 2)
        i = 1
        di = (d + i*n) % self._mSize
        # Invariant: self._hasKey(key, dj) = False and it is not None, for all 0 <= j < i; di really is di
        #               where dj = (d + j * n) % self._mSize
        while not self._hasKey(key, di) and self._data[di] is not None:
            if self._isTomb(di) and prev is None:
                prev = di
            i += 1
            di = (d + i*n) % self._mSize
        
        if self._hasKey(key, di) or prev is None:
            return di
        else:
            return prev

    def _hasKey(self, key, i):
        if self._data[i] is None or self._isTomb(i):
            return False
        else:
            return self._data[i][0] == key

    def _isTomb(self, i):
        if self._data[i] is None:
            return False
        else:
            return self._data[i] == self._tomb

    def _tooManyTombs(self):
        return (self._nTombs / self._mSize) > 0.2

    def _clearTombs(self):
        self._resize(self._mSize)

    def _isAtMaxLoadFactor(self):
        return self._curSize / self._mSize > self._maxLoadFactor

    def _doubleSize(self):
        self._resize(2 * self._mSize)

    def _resize(self, newSize):
        oldData = self._data

        self._mSize = newSize
        self._curSize = 0
        self._nTombs = 0
        self._data = [None] * self._mSize

        for pair in oldData:
            if pair is not None and pair != self._tomb:
                self.add(pair[0],pair[1])