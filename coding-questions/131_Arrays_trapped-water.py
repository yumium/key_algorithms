# Source: https://leetcode.com/problems/trapping-rain-water/

from collections import Counter

class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Given:
            height: A list of heights of bars
                0 <= height[n] <= 1E5
                1 <= len(height) <= 2E4
        Return:
            # of squares of water it can trap after rainin

        Obs:
        - There are no walls on left and right end
        - Height of water blocks cannot be higher than highest column
        '''
        freq = Counter(height)  # height => # of columns with that height, ignore height of 0
        if 0 in freq:
            del freq[0]

        if len(freq) == 0: # All columns are of height 0
            return 0

        res = 0
        i = 0
        j = len(height)-1
        column = sum(freq.values())  # The number of columns with height at least `h`
        for h in range(1, max(freq.keys())+1):
            while height[i] < h:
                i += 1
            while height[j] < h:
                j -= 1
            
            res += (j-i+1) - column
            if h in freq:
                column -= freq[h]
        
        return res

