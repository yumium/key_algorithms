# Source: https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        Given:
            mat: m x n binary matrix
                1 <= m, n <= 1E4
                At least one 0 in mat
        Return:
            a matrix of same size, with dist. of nearest 0 for each cell (taxi cab distance)
        '''

        m = len(mat)
        n = len(mat[0])
        inf = m + n

        res = [None]*m
        for i in range(0, m):
            res[i] = [None]*n

        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = inf
                    if i-1 >= 0:
                        res[i][j] = min(res[i][j], 1+res[i-1][j])
                    if j-1 >= 0:
                        res[i][j] = min(res[i][j], 1+res[i][j-1])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m:
                    res[i][j] = min(res[i][j], 1+res[i+1][j])
                if j+1 < n:
                    res[i][j] = min(res[i][j], 1+res[i][j+1])

        return res