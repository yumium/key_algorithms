# Source: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        Given:
            matrix: m by n integer matrix
                1 <= m, n <= 200            N
                0 <= matrix[i][j] <= 2E31-1
        Return:
            Length of longest increasing path
                e[i] < e[i+1]
        
        Bruteforce => 
        TIME: O(N*M * 4 ^ (N*M))
        SPACE: O(N*M)

        Obs/Ideas:
        - There is always candidate paths (just element itself)
        - DP approach?

        TIME: O(N log N)
        SPACE: O(N)
        '''
        M = len(matrix)
        N = len(matrix[0])
        schedule = [(matrix[i][j], i, j) for i in range(M) for j in range(N)]
        schedule.sort(reverse=True)

        longestFrom = [[None]*N for _ in range(M)]

        for elem, i, j in schedule:
            cur_max = 1
            adj = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for i1, j1 in adj:
                if 0 <= i1 < M and 0 <= j1 < N and matrix[i1][j1] > elem:
                    cur_max = max(cur_max, 1 + longestFrom[i1][j1])
            longestFrom[i][j] = cur_max
        
        return max([max(row) for row in longestFrom])
        
