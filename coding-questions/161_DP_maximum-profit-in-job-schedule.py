# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        Given:
            startTime: Array of job start times
            endTime: Array of job end times
            profit: Array of job profits
                1 <= len(startTime) = len(endTime) = len(profit) <= 5E4
                1 <= startTime[i] < endTime[i] <= 1E9
                1 <= profit[i] <= 1E4
            Each job i occupy time slots [startTime[i] .. endTime[i])

        Return:
            Maximum profit you can make s.t. no 2 jobs are overlapping

        Obs:
        - Will make at least some profit, as can always take 1 job
        - Greedy, DP?

        TIME: O(N log N)
        SPACE: O(N), where N = # of tasks
        '''
        N = len(startTime)

        for i in range(N):
            startTime[i] = (startTime[i], endTime[i], profit[i])
        startTime.sort()

        MAX_END_TIME = int(1E9)
        max_from = [[MAX_END_TIME+1, 0]]   # latest task start time for new profit => new profit

        for start, end, profit in startTime[::-1]:
            i = self.search(max_from, end)
            cur_profit = profit if i == -1 else profit + max_from[i][1]
            if cur_profit > max_from[-1][1]:
                max_from.append([start, cur_profit])

        return max_from[-1][1]

    def search(self, max_from, start):
        N = len(max_from)
        i, j = 0, N
        # Invariant: max_from[0..i)[0] >= start; max_from[j..N) < start
        while i < j:
            m = (i+j) // 2
            if max_from[m][0] >= start:
                i = m+1
            else:
                j = m
            
        if i == 0:
            return -1
        else:
            return i-1

