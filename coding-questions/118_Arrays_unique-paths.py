# Source: https://leetcode.com/problems/unique-paths/

from math import factorial

class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        '''
        Given:
            m, n: dimensions of grid
                1 <= m, n <= 100
        Return:
            # of possible unique paths from top left to bottom right

        Path: <D,D,R,R>
        Obs:
        - Paths to bottom right have equal length
        - Paths contain same # of Ds and Rs
        '''
        # TIME: O(M+N)
        # SPACE: O(1)

        return factorial(m+n-2) // ( factorial(n-1) * factorial(m-1) )

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for i in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        
        return grid[m-1][n-1]