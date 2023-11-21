import math
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        Given:
            points: Array of 2D coordinates
                1 <= len(points) <= 300     N
                -1E4 <= points[i][0], points[i][1] <= 1E4
                All points unique
        Return:
            Max # of points that lie on the same straight line

        Ideas/Obs:
        - Lines don't need to be vertical, horizontal, or diagonal. They can be in any angle between 2 points
        - If len(points) = 1, return 1. Otherwise answer is at least 2 (2 points form a line)

        TIME: O(N^2 log M)  where M = max(abs(points[i][_]))
        SPACE: O(N)
        '''
        if len(points) == 1:
            return 1

        N = len(points)
        cur_max = 0
        for i in range(N):
            gradients = self.gradients(points, i)   # gradient keys with all other points
            tally = dict(Counter(gradients))        # gradient key => count
            i_max = max(tally.values()) + 1         # maximum # of points on a line including points[i]
            cur_max = max(cur_max, i_max)

        return cur_max

    def gradients(self, points, i):
        deltas = []     # (dy, dx, pos) where pos is True if the gradient is positive. Stores (1,0,True) for horizontal gradients, (0,1,True) for vertical gradients, and (abs(dy),abs(dx),pos) where dy/dx is in simplest fraction. These form keys for lines.
        for j in [k for k in range(len(points)) if k != i]:
            # delta = points[i] - points[j]
            dy = points[i][1] - points[j][1]
            dx = points[i][0] - points[j][0]
            if dy == 0:
                deltas.append((0, 1, True))
            elif dx == 0:
                deltas.append((1, 0, True))
            else:
                gcd = math.gcd(abs(dy),abs(dx))
                deltas.append((abs(dy // gcd), abs(dx // gcd), dy*dx > 0))
        return deltas

