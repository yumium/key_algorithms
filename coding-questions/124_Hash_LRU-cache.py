# Source: https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        '''
        DTI:
        - head points to dummy node
        - tail points to last node
        - keys[k] points at node in front of k's node
        - keys is current mapping of k->v
        - linked list is in access order
        - capacity of linked list is not larger than `capacity`
        - capacity is current linked list capacity
        '''
        assert 1 <= capacity <= 3000
        self.max_capacity = capacity
        self.capacity = 0
        self.head = Node('DUMMY', 'DUMMY')
        self.tail = self.head
        self.keys = {}

    def get(self, key: int) -> int:
        '''
        Given:
            key: the key
                0 <= key <= 1E4
        Return:
            the value of the key if exists, otherwise -1
        '''
        if key in self.keys:
            node = self.keys[key].next
            if self.tail != node:
                self.keys[key].next = node.next
                self.tail.next = node
                self.keys[node.next.key] = self.keys[key]
                self.keys[key] = self.tail
                self.tail = self.tail.next
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        '''
        Given:
            key:
            value:
                0 <= value <= 1E5
        Return:
            None. Add/Update key-value pair. Evict least recently used key if capacity full.
        '''
        if key in self.keys:
            node = self.keys[key].next
            node.val = value
            if self.tail != node:
                self.keys[key].next = node.next
                self.tail.next = node
                self.keys[node.next.key] = self.keys[key]
                self.keys[key] = self.tail
                self.tail = self.tail.next
        else:
            self.keys[key] = self.tail
            self.tail.next = Node(key, value)
            self.tail = self.tail.next
            if self.capacity == self.max_capacity:
                del self.keys[self.head.next.key]
                self.keys[self.head.next.next.key] = self.head
                self.head.next = self.head.next.next
            else:
                self.capacity += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)