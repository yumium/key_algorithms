# Source: https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Given:
            matrix: M x N binary matrix (of 0s and 1s)
                M = len(matrix), N = len(matrix[0])
                1 <= M, N <= 300
        Return:
            Largest square containing 1s and return its area

        Bruteforce:
        TIME: O(M*N*min(M,N))
        SPACE: O(1)

        Obs:
        - Rolling window idea? track the # of 1s
        - Connected components?
        - Find rectangles?
        '''
        M, N = len(matrix), len(matrix[0])
        cur_max = 0
        square_end = [[None]*N for _ in range(M)]
        for i, j in [(0,j) for j in range(N)] + [(i,N-1) for i in range(1,M)]:
            while i < M and j >= 0:
                if matrix[i][j] == '0':
                    square_end[i][j] = 0
                else:
                    adj = []
                    for r, c in [(i-1, j), (i-1, j-1), (i, j-1)]:
                        if r >= 0 and c >= 0:
                            adj.append(square_end[r][c])
                        else:
                            adj.append(0)
                    square_end[i][j] = min(adj) + 1
                cur_max = max(cur_max, square_end[i][j])
                i += 1; j -= 1

        return cur_max ** 2

