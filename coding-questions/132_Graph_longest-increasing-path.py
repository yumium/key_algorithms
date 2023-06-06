# Source: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        Given:
            matrix: A grid of integers
                at least 1x1
                1 <= m, n <= 200
        Return:
            The length of longest increasing path in `matrix`
        
        Obs:
        - Will return at least 1, as a path of a single element is an increasing sequence
        - Whenever `visit` explores a node, it will be the longest increasing path from there because the nodes currently in `seen` have to be strictly smaller
        '''
        longest = 0  # Current longest increasing path

        rows = len(matrix)
        cols = len(matrix[0])

        # The longest path starting from (i,j)
        longest_paths = [[None]*cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                longest = max(longest, self.visit(i, j, set(), matrix, longest_paths))

        return longest

        
    def visit(self, i, j, seen, matrix, longest_paths):
        '''Visit all paths from (i,j), return longest increasing sequence from (i,j) given `seen`'''
        seen.add((i,j))
        if longest_paths[i][j] is not None:
            return longest_paths[i][j]

        longest = 0 # Current longest increasing path from (i,j) given `seen`
        val = matrix[i][j]
        rows = len(matrix)
        cols = len(matrix[0])

        # Up
        if i-1 >= 0 and ((i-1,j)) not in seen and matrix[i-1][j] > val:
            longest = max(longest, self.visit(i-1, j, seen, matrix, longest_paths))
            seen.remove((i-1,j))

        # Down
        if i+1 < rows and ((i+1,j)) not in seen and matrix[i+1][j] > val:
            longest = max(longest, self.visit(i+1, j, seen, matrix, longest_paths))
            seen.remove((i+1,j))

        # Left
        if j-1 >= 0 and ((i,j-1)) not in seen and matrix[i][j-1] > val:
            longest = max(longest, self.visit(i, j-1, seen, matrix, longest_paths))
            seen.remove((i,j-1))

        # Right
        if j+1 < cols and ((i,j+1)) not in seen and matrix[i][j+1] > val:
            longest = max(longest, self.visit(i, j+1, seen, matrix, longest_paths))
            seen.remove((i,j+1))

        longest_paths[i][j] = 1+longest

        return 1+longest

