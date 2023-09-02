# Source: https://leetcode.com/problems/decode-string/solutions/

class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Given:
            s: Encoded string
                1 <= len(s) <= 30
                Assume s is valid (no parsing needed)
                1 <= integers in s <= 300
        Return:
            Decoded string
                Output length will not exceed 1E5
        
        TIME: O(N^2)
        SPACE: O(N^2)
        '''
        res = ''
        N = len(s)

        i = 0
        while i < N:
            if s[i].isnumeric():
                number = ''
                while s[i].isnumeric():
                    number += s[i]
                    i += 1
                mult = int(number)
                inner, i = self.get_repeat(s, i)
                res += mult * self.decodeString(inner)
            else:
                res += s[i]
                i += 1

        return res
        

    def get_repeat(self, s, i):
        inner = ''
        num_left = 1  # number of [ - number of ]
        i += 1
        while num_left > 0:
            if s[i] == '[':
                num_left += 1
            elif s[i] == ']':
                num_left -= 1
                if num_left == 0:
                    return (inner, i+1)

            inner += s[i]
            i += 1

        

        