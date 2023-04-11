from heap import MaxHeap

class PriorityQueue:
    def __init__(self):
        self.queue = MaxHeap([])  # Elements are tuples of (priority, elem)

    def insert(self, x, key):
        '''
        Inserts task `x` with priority `key`
        '''
        self.queue.insert((key,x))

    def maximum(self):
        '''
        Returns the element with the highest priority
        '''
        return self.queue.maximum()[1]

    def extract_max(self):
        '''
        Removes and returns the element with the highest priority
        '''
        return self.queue.extract_max()[1]
    
    def increase_key(self, x, old_key, key):
        '''
        Increase priority of `x` to `key`
        '''
        return self.queue.increase_val((old_key,x), (key,x))
