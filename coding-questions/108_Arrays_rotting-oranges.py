# Source: https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Given:
            grid: m by n grid, each cell has value in [0,1,2]
                1 <= m, n <= 10
        Return:
            min # of minutes that must elapse until no cell has a fresh orange (can be 0)
            Return -1 if impossible (e.g., all oranges are fresh)
        '''
        num_fresh = 0
        num_elapsed = 0
        rottens = set()  # Rotten oranges to check

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    rottens.add((i,j))

        repeated = False
        while repeated == False:
            rottens = self.update(grid, rottens)
            repeated = len(rottens) == 0
            num_fresh -= len(rottens)
            num_elapsed += 1

        if num_fresh > 0:
            return -1
        else:
            return num_elapsed - 1
        
    def update(self, grid, rottens):
        rows = len(grid)
        cols = len(grid[0])

        new_rot = set()
        for i,j in rottens:
            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                new_rot.add((i-1,j))
            if i+1 < rows and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                new_rot.add((i+1,j))
            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                new_rot.add((i,j-1))
            if j+1 < cols and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                new_rot.add((i,j+1))
        
        return new_rot
