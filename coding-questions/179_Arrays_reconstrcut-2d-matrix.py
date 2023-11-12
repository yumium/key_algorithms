# Source: https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        N = len(colsum)
        numTwos = len([i for i in range(N) if colsum[i] == 2])

        mat = [[None]*N for _ in range(2)]
        if not self.canFill(upper, lower, colsum):
            return []

        ULeft = upper - numTwos
        LLeft = lower - numTwos
        for i in range(N):
            if colsum[i] == 0:
                mat[0][i] = 0
                mat[1][i] = 0
            elif colsum[i] == 2:
                mat[0][i] = 1
                mat[1][i] = 1
            elif ULeft > 0:
                mat[0][i] = 1
                mat[1][i] = 0
                ULeft -= 1
            else:
                mat[0][i] = 0
                mat[1][i] = 1
                LLeft -= 1
        
        return mat

    def canFill(self, upper, lower, colsum):
        N = len(colsum)
        numOnes = len([i for i in range(N) if colsum[i] == 1])
        numTwos = len([i for i in range(N) if colsum[i] == 2])

        return numTwos <= upper and numTwos <= lower and numOnes == (upper - numTwos) + (lower - numTwos)


