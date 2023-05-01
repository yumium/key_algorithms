# Source: https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board, word):
        '''
        Given:
            board: m x n grid of characters
                1 <= m, n <= 6
            word: The word string
                1 <= len(word) <= 15
            board & word consist of only upper and lower case English letter
        Return:
            If word can be constructed from letters sequentially in adjacent cells
            Same letter cannot be used twice
        '''
        # TIME: O((M*N)^2)
        # SPACE: O(M*N)

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.search(board, word, i, j):
                    return True

        return False

    def search(self, board, word, i, j):
        '''
        Return if `word` can be found in unseen nodes in `board` starting from position (i,j)
        Pre:
        - len(word) >= 1
        - (i,j) not seen
        '''
        tmp = board[i][j]
        board[i][j] = '#'  # Mark as seen
        m = len(board)
        n = len(board[0])

        if tmp != word[0]:
            board[i][j] = tmp  # Restore
            return False
        
        if len(word) == 1:
            return True
        else:
            if i-1 >= 0 and self.search(board, word[1:], i-1, j):
                return True
            if i+1 < m and self.search(board, word[1:], i+1, j):
                return True
            if j-1 >= 0 and self.search(board, word[1:], i, j-1):
                return True
            if j+1 < n and self.search(board, word[1:], i, j+1):
                return True
            
        board[i][j] = tmp  # Restore
        return False