# Source: https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Given:
            matrix: M x N integer matrix
            target: The target integer
                Each row is non-decreasing
                Starting pivot is strictly larger than last element of previous row
        Return:
            Whether `target` is in matrix

        Bruteforce:
        TIME: O(M*N)
        SPACE: O(1)

        TIME: O(logM) + O(logN) = O(log(M*N))
        SPACE: O(1)
        '''
        M, N = len(matrix), len(matrix[0])

        # Search row, find row `i` that is the largest `i` satisfying matrix[i][0] <= target
        i, j = 0, M
        # Invariant: matrix_first_col[0..i) <= target; matrix_first_col[j..M) > target
        while i < j:
            m = (i+j) // 2
            if matrix[m][0] <= target:
                i = m+1
            else:
                j = m
        
        if j == 0:
            return False

        # Search within row `j-1`
        row = matrix[j-1]
        i, j = 0, N
        # Invariant: row[0..i) < target; row[j..N) >= target
        while i < j:
            m = (i+j) // 2
            if row[m] < target:
                i = m+1
            else:
                j = m
        
        if j < N and row[j] == target:
            return True
        else:
            return False

