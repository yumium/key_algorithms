# Source: https://leetcode.com/problems/maximum-frequency-stack/

import heapq

class FreqStack:

    def __init__(self):
        self.stack = [] # max heap
        self.freq = {}  # element -> frequency in stack
        self.num_inserted = 0

    def push(self, val: int) -> None:
        '''
        Given:
            val: The value to push
                val >= 0
        Return:
            Pushes `val` to the top of stack
        
        TIME: O(log N)
        '''
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

        heapq.heappush(self.stack, (-self.freq[val], -self.num_inserted, val))
        self.num_inserted += 1

    # Obs:
    # - Finding the most frequent elements is slow
        # MaxHeap (frequency, top_index, element)
        # How to push to this heap?
        # 
    # - Finding the top index for each element is slow
    def pop(self) -> int:
        '''
        Return:
            The top element of the most frequent element in stack
            Return elements closer to top to break ties
        
        TIME: O(log N)
        '''
        assert len(self.stack) > 0

        _, _, res = heapq.heappop(self.stack)
        if self.freq[res] == 1:
            del self.freq[res]
        else:
            self.freq[res] -= 1

        return res

class FreqStackOptimal(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()