from abc import ABC, abstractmethod

class DisjointSet(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def make_set(self, x):
        pass
    
    @abstractmethod
    def find_set(self, x):
        pass
    
    @abstractmethod
    def union(self, x, y):
        pass

class ArrayDisjointSet(DisjointSet):
    def __init__(self, MAX_VAL=100):
        self.arr = [None]*(MAX_VAL+1)
        self.MAX_VAL = MAX_VAL
        
    def make_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        self.arr[x] = x
        
    def find_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        return self.arr[x]
    
    def union(self, x, y):
        assert 0 <= x <= self.MAX_VAL and 0 <= y <= self.MAX_VAL
        p_x, p_y = self.find_set(x), self.find_set(y)
        for i in range(self.MAX_VAL+1):
            if self.arr[i] == p_x:
                self.arr[i] = p_y

class LinkedListDisjointSet(DisjointSet):
    def __init__(self, MAX_VAL=100):
        self.pointer = [None]*(MAX_VAL+1)  # Storing the node
        self.MAX_VAL = MAX_VAL

    def make_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        elem = self._Element(None, x, None)
        elem.set = self._DisjointSet(elem, elem) 
        self.pointer[x] = elem
        
    def find_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        return self.pointer[x].set.head.val
    
    def union(self, x, y):
        x_length = self.pointer[x].set.length
        y_length = self.pointer[y].set.length
    
        # Append shorter list onto longer list
        if x_length >= y_length:
            self._join(x, y)
        else:
            self._join(y, x)

    def _join(self, x, y):
        # append y to x
        x_set = self.pointer[x].set
        y_set = self.pointer[y].set
        x_set.tail.next = y_set.head
        x_set.tail = y_set.tail
        
        node = y_set.head
        while node is not None:
            node.set = x_set
            node = node.next

        x_set.length += y_set.length

    class _DisjointSet:
        def __init__(self, head, tail, length=1):
            self.head = head
            self.tail = tail
            self.length = length

    class _Element:
        def __init__(self, set, val, next):
            self.set = set
            self.val = val
            self.next = next

class DisjoinSetForest(DisjointSet):
    def __init__(self, MAX_VAL=100):
        self.p = [None]*(MAX_VAL+1)  # Parent pointer
        self.h = [1]*(MAX_VAL+1)  # Height of tree rooted at this index
        self.MAX_VAL = MAX_VAL
    
    def make_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        self.p[x] = x
    
    def find_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        while self.p[x] != x:
            x = self.p[x]
        return x
    
    def union(self, x, y):
        x_p = self.find_set(x)
        y_p = self.find_set(y)
        # Link-By-Height heuristic
        if self.h[x_p] < self.h[y_p]:
            self.p[x_p] = y_p
        elif self.h[x_p] > self.h[y_p]:
            self.p[y_p] = x_p
        else:
            self.p[y_p] = x_p
            self.h[x_p] += 1

class DisjointSetForestOpt(DisjointSet):
    def __init__(self, MAX_VAL=100):
        self.p = [None]*(MAX_VAL+1)  # Parent pointer
        self.r = [1]*(MAX_VAL+1)  # Rank of tree rooted at this index
        self.MAX_VAL = MAX_VAL
    
    def make_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        self.p[x] = x
    
    def find_set(self, x):
        assert 0 <= x <= self.MAX_VAL
        if self.p[x] != x:
            # Path compression
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x_p = self.find_set(x)
        y_p = self.find_set(y)
        # Link-By-Rank heuristic
        if self.r[x_p] < self.r[y_p]:
            self.p[x_p] = y_p
        elif self.r[x_p] > self.r[y_p]:
            self.p[y_p] = x_p
        else:
            self.p[y_p] = x_p
            self.r[x_p] += 1



def test_ds(ds_class):
    print(f'Testing class {ds_class.__name__}')
    ds = ds_class()
    ds.make_set(0)
    ds.make_set(1)
    ds.make_set(2)
    assert ds.find_set(1) == 1
    ds.union(1,2)
    assert ds.find_set(1) == ds.find_set(2), f'{ds.find_set(1)} is not equal to {ds.find_set(2)}'
    assert ds.find_set(1) != ds.find_set(0)
    ds.union(0,2)
    assert ds.find_set(1) == ds.find_set(0), f'{ds.find_set(1)} is not equal to {ds.find_set(0)}'

if __name__ == '__main__':
    classes = [ArrayDisjointSet, LinkedListDisjointSet, DisjoinSetForest, DisjointSetForestOpt]
    for c in classes:
        test_ds(c)
    print(f'Test completed without errors for all classes')