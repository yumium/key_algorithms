# Source: https://leetcode.com/problems/sudoku-solver/

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        '''
        Given:
            board: 2D array representing the initial board
                len(board) = len(board[i]) = 9      N
                board[i][j] is digit ('1'-'9') or '.'
        Return:
            Modify the board in-place to contain the solution
            Exactly one solution exist for every input board

        Idea:
        - Keep track for each cell the digits that can be placed while maintaining the invariant that it's a valid partial sudoku board
        - Pick a cell to expand, prioritise the one with lease # of possibilities
        - Try each digit for that cell, prune the rest of cells and iterate 
            - Terminate when there are no empty cells left
            - Backtrack when there is an empty cell w/ no valid digits to put

        TIME: O(N^(N^2))
        SPACE: O(N^5)
        '''
        N = len(board)
        empty_cells = [] # (list of possible values, row, col)
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    empty_cells.append(([str(d) for d in range(1,10)], i, j))

        if len(empty_cells) == 0:
            return
        
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    self.prune(i, j, board[i][j], empty_cells)

        sol = self.solveSudokuRecurse(board, empty_cells)

        for i in range(N):
            for j in range(N):
                board[i][j] = sol[i][j]

    def solveSudokuRecurse(self, board, empty_cells):
        '''
        Pre:
            `board` is current configuration
            `empty_cells` contain empty cells in `board` with valid values
        Return:
            Solution of board or None if not possible
        '''
        if len(empty_cells) == 0:
            return board
    
        # Use a heap?
        empty_cells.sort()
        fill, row, col = empty_cells.pop(0)

        if len(fill) == 0:
            return None

        for v in fill:
            board_new = self.copy_board(board)
            cells_new = self.copy_cells(empty_cells)
            board_new[row][col] = v
            self.prune(row, col, v, cells_new)
            sol = self.solveSudokuRecurse(board_new, cells_new)
            if sol is not None:
                return sol

        return None

    def prune(self, row, col, val, empty_cells):
        # Prunes `empty_cells` in-place
        block_row = row // 3
        block_col = col // 3
        
        for fill, i, j in empty_cells:
            if i == row or j == col or (i//3 == block_row and j//3 == block_col):
                if val in fill:
                    fill.remove(val)

    def copy_board(self, board):
        return [row.copy() for row in board]
    
    def copy_cells(self, empty_cells):
        return [(fill.copy(), row, col) for fill, row, col in empty_cells]

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
sol.solveSudoku(board)
print(board)
