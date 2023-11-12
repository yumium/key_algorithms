# Source: https://leetcode.com/problems/n-queens/solutions/19808/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        Given:
            n: Side length of board
                1 <= n <= 9
        Return:
            List of all solutions to the N-queens problem
        
        Obs:
        - Solution must satisfy ever row and column contains exactly 1 queen
        
        Idea:
        - Put queens row by row and backtrack

        Bruteforce => try all possible N-queen config
        - TIME: O(N^(2*N) * N)
        - SPACE: O(N^2)
        
        TIME: O(N^N)
        SPACE: O(N^2)
        '''
        solutions = []
        board = [['E']*n for _ in range(n)]  # E => Empty & no attack, Q => Queen, A => Attacked
        self.placeQueenAtRow(board, 0, [], [], solutions)

        return solutions

    def placeQueenAtRow(self, board, row, queens, blocks, solutions):
        n = len(board)
        for col in range(n):
            if board[row][col] == 'E':
                coords = self.blockCoords(n, row, col)
                
                # Check attacks
                noAttack = True
                for i, j in coords:
                    if board[i][j] == 'Q':
                        noAttack = False
                        break

                # Recurse
                if noAttack:
                    # Update board
                    queens.append((row, col))
                    board[row][col] = 'Q'
                    block = []
                    for i, j in coords:
                        if board[i][j] == 'E':
                            board[i][j] = 'A'
                            block.append((i,j))
                    blocks.append(block)

                    # Recurse or add solution
                    if row == n-1:
                        solutions.append(self.stringifyBoard(board))
                    else:
                        self.placeQueenAtRow(board, row+1, queens, blocks, solutions)

                    # Revert board
                    r, c = queens.pop()
                    board[r][c] = 'E'

                    bs = blocks.pop()
                    for r, c in bs:
                        board[r][c] = 'E'

    def blockCoords(self, n, row, col):
        up = [(-i, 0) for i in range(1, n)]
        down = [(i, 0) for i in range(1, n)]
        left = [(0, -i) for i in range(1, n)]
        right = [(0, i) for i in range(1, n)]
        topLeft = [(-i, -i) for i in range(1, n)]
        topRight = [(-i, i) for i in range(1, n)]
        bottomLeft = [(i, -i) for i in range(1, n)]
        bottomRight = [(i, i) for i in range(1, n)]

        dirs = up + down + left + right + topLeft + topRight + bottomLeft + bottomRight
        res = [(i+row,j+col) for i, j in dirs if 0 <= i+row < n and 0 <= j+col < n]
        return res

    def stringifyBoard(self, board):
        # print(self.printRows(board))
        res = []
        for row in board:
            rowString = ''
            for item in row:
                if item == 'Q':
                    rowString += 'Q'
                else:
                    rowString += '.'
            res.append(rowString)
        
        return res

