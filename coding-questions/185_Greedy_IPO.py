# Source: https://leetcode.com/problems/ipo/
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''
        Given:
            k: Max # of distinct projects to finish before IPO  K
            w: Starting capital                                 W
            profits: Array of profit for each project           N
            capital: Array of capital for each project          N

                1 <= k <= 1E5
                0 <= w <= 1E9
                1 <= N <= 1E5
                0 <= profits[i] <= 1E4
                0 <= capital[i] <= 1E9
        Return:
            Final maximized capital
        
        Obs/Ideas:
        - profits >= 0, so we always recouperate our capital
        - we do projects sequentially, starting the next only after finishing the previous
        - order of projects don't affect final capital
            - execute in order (capital[i], -profit[i]) ?
        - we should do min(k, max # of distict projects given initial capital)

        Bruteforce => try all sequences of min(K, N) distinct projects
        TIME: O(min(K,N)! * min(K,N))
        SPACE: O(min(K,N))

        - DP approach?
            - Increase k
            - Increase i
        
        - Max capital ending on project i

        - DIY
            - At each stage, I have a list of projects I can do
            - I will select the one with the maximum profit
            - Recurse until 1) meet k or 2) no undone projects left that I can afford to start
        - My capital never decreases => scope of projects monotonically increases
        - Answer can be 0

        TIME: O(K log N) + O(N log N)
        SPACE: O(N)
        '''
        N = len(profits)
        num_projects = 0
        i = 0
        projects = sorted([(c,p) for c, p in zip(capital, profits)])    # projects[0..i) can be afforded
        inscope_projects = []   # -1*profits of projects valid to start next
        
        while num_projects < k:
            while i < N and projects[i][0] <= w:
                heapq.heappush(inscope_projects, -projects[i][1])
                i += 1

            if len(inscope_projects) == 0:
                break
            else:
                w += -1 * heapq.heappop(inscope_projects)
                num_projects += 1

        return w
