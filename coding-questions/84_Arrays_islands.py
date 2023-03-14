# Source: https://leetcode.com/problems/number-of-islands/submissions/913402113/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.dfs(grid, (i,j))

        return num_islands
        
    def dfs(self, grid, root):
        """
            Visit all the nodes reachable by `root` and mark the field to be `-1`
        """
        ROWS = len(grid)
        COLS = len(grid[0])

        i, j = root
        grid[i][j] = '-1'  # Mark as visited
    
        if i-1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, (i-1,j))
        if i+1 < ROWS and grid[i+1][j] == '1':
            self.dfs(grid, (i+1,j))
        if j-1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, (i,j-1))
        if j+1 < COLS and grid[i][j+1] == '1':
            self.dfs(grid, (i,j+1))
        return
