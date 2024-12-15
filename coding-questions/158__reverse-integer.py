# Source: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        '''
        Given:
            x: Signed 32 bit integer
        Return:
            The reverse of `x` as integer, or 0 if outside range [-2E31, 2E31-1]
        '''
        result = 0

        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            tail = x % 10
            new_result = result*10 + tail
            if new_result < -2**31 or new_result > 2**31-1:
                return 0
            x = x // 10
            result = new_result
        
        return sign * result

    def reverse2(self, x: int) -> int:
        if x == 0:
            return 0
    
        sign = -1 if x < 0 else 1

        reverse = str(abs(x)).rstrip('0')[::-1]

        if not self.fit_32(reverse, sign):
            return 0
        else:
            return sign*int(reverse)

    def fit_32(self, x, sign):
        '''
        x is a string of positive integer
        '''
        boundary = str(2**31) if sign == -1 else str(2**31-1)

        if len(x) == len(boundary):
            return x <= boundary
        else:
            return len(x) < len(boundary)
