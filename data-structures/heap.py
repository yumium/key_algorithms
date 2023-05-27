class MaxHeap:
    def __init__(self, arr=None):
        self.heap = arr

    def make_max_heap(self, arr):
        '''
        Create a max heap from an array `arr`
        This operation is O(N)
        '''

        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self._max_heapify(i)

    def maximum(self):
        assert self.heap is not None and len(self.heap) > 0

        return self.heap[0]

    def extract_max(self):
        assert self.heap is not None and len(self.heap) > 0
        
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        out = self.heap.pop()
        if len(self.heap) > 0:
            self._max_heapify(0)
        return out

    def insert(self, elem):
        if self.heap is None:
            self.heap = [elem]
        else:
            self.heap.append(elem)
            # Bubble up
            self._bubble_up(len(self.heap)-1)

    def remove(self, elem): 
        assert self.heap is not None
        '''
        Removes an element with value `elem`
        Return True if successful, False otherwise
        '''
        assert self.heap is not None and len(self.heap) >= 1
        size = len(self.heap)
        
        i = 0
        while i < size and self.a[i] != elem:
            i += 1

        if i == size:
            return False
        elif i == size-1:
            self.heap.pop()
        else:
            # Swap the element to delete with the last element in the heap
            self.heap[i] = self.heap.pop()
            if self.heap[i] > elem:
                # Bubble up
                self._bubble_up(i)
            elif self.heap[i] < elem:
                self._max_heapify(i)

        return True

    def increase_val(self, old_val, new_val):
        '''
        Increase first element in heap with value `old_val` to `new_val`
        Returns True if sucessful, False if `old_val` is not in the heap
        '''
        assert self.heap is not None and new_val >= old_val

        try:
            i = self.heap.index(old_val)
        except ValueError:
            return False
        
        self.heap[i] = new_val
        self._bubble_up(i)
        return True

    def _bubble_up(self, i):
        assert self.heap is not None and 0 <= i < len(self.heap)
        
        while i != 0 and self.heap[(i-1)//2] < self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1) // 2
        return i

    def _max_heapify(self, i):
        '''
        Given an index `i` of the heap and assuming left and right trees (if exist) of `i` are max heaps, make tree at `i` a max heap.
        This operation is O(logN)
        '''

        assert 0 <= i < len(self.heap)

        a, size, iMax = self.heap, len(self.heap), i
        if 2*i+1 < size and a[2*i+1] > a[iMax]:
            iMax = 2*i+1
        if 2*i+2 < size and a[2*i+2] > a[iMax]:
            iMax = 2*i+2
        if iMax != i:
            a[i], a[iMax] = a[iMax], a[i]
            self._max_heapify(iMax)
