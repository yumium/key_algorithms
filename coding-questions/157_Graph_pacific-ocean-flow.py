# Source: https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Given:
            heights: M x N integer matrix for square height above sea level
                0 <= heights[r][c] <= 1E5
                1 <= m, n <= 200
        Return:
            A list of coordinates of cells where water can flow to both oceans

        Edge: (a, b) if a can flow to b
        In here we do the reverse
        
        TIME: O(M*N)
        SPACE: O(M*N)
        '''
        M, N = len(heights), len(heights[0])
        pacific = set()
        for c in range(N):
            if (0, c) not in pacific:
                self.visit(heights, pacific, 0, c)
        for r in range(M):
            if (r, 0) not in pacific:
                self.visit(heights, pacific, r, 0)
        
        atlantic = set()
        for r in range(M):
            if (r, N-1) not in atlantic:
                self.visit(heights, atlantic, r, N-1)
        for c in range(N):
            if (M-1, c) not in atlantic:
                self.visit(heights, atlantic, M-1, c)

        return [list(common) for common in pacific & atlantic]

    # Edges are towards cells of at least the current height
    def visit(self, heights, seen, r, c):
        M, N = len(heights), len(heights[0])
        seen.add((r,c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r_new, c_new = r+dr, c+dc
            if 0 <= r_new < M and 0 <= c_new < N and heights[r_new][c_new] >= heights[r][c] and (r_new, c_new) not in seen:
                self.visit(heights, seen, r_new, c_new)
