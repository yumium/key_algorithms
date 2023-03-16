# Source: https://leetcode.com/problems/rotate-image/

import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Given:
            matrix: n*n, 1 <= n <= 20
                -1000 <= val <= 1000
        Return: 
            Do not return anything, modify matrix in-place instead. Rotated to right by 90 degrees
        """
        n = len(matrix)
        for i in range(0, math.ceil(n/2)):  # Ceiling function to treat 
            for j in range(0, n//2):
                coords = [(i,j)]
                x, y = i, j
                for _ in range(3):
                    x, y = y, n-1-x
                    coords.append((x,y))
                print(coords)
                values = [matrix[x][y] for x, y in coords]
                values.insert(0, values.pop())
                for v, (x,y) in zip(values, coords):
                    matrix[x][y] = v
        


