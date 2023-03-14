class FIFOqueue:
    '''
    This is a circular array implementation of the FIFO queue.

    Abstraction function:
        If iOut <= iIn: 
            If isFull: [iOut..maxSize) ++ [0..iIn)
            else: [iOut..iIn)
        If iOut > iIn: [iOut..maxSize) ++ [0..iIn)
    '''

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None] * maxSize
        self.iOut = 0
        self.iIn = 0
        self._isFull = False

    def enqueue(self, val):
        # Pre: !isFull()
        self.arr[self.iIn] = val
        self.iIn = (self.iIn + 1)%self.maxSize
        if self.iIn == self.iOut: 
            self._isFull = True

    def dequeue(self):
        # Pre: !isEmpty()
        out = self.arr[self.iOut]
        self.iOut = (self.iOut + 1)%self.maxSize
        self._isFull = False
        return out

    def isFull(self):
        return self._isFull

    def isEmpty(self):
        return self.iIn == self.iOut and not self._isFull

    def curSize(self):
        if self.isFull():
            return self.maxSize
        else:
            return (self.iIn - self.iOut)%self.maxSize