# Source: https://leetcode.com/problems/min-stack/

class MinStack:
    '''
    - O(1) time for all operations
    - Assume last 3 methods are only called on non-empty stacks
    - -2**31 <= val <= 2**31 - 1
    - At most 3E4 calls made to push, pop, top, and getMin

    DTI:
    - self.stack[i] = elements[i] - min(elements[0..i))
    - self.minimum = min(elements[0..N)), when len(self.stack) > 0
    '''
    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(0)
            self.minimum = val

        else:
            self.stack.append(val-self.minimum)
            if val < self.minimum:
                self.minimum = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val <= 0:
            self.minimum -= val
        return val + self.minimum

    def top(self) -> int:
        val = self.stack[-1]
        min_value = self.minimum
        if val <= 0:
            min_value -= val
        return val + min_value

    def getMin(self) -> int:
        return self.minimum