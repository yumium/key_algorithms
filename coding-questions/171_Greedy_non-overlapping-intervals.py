# Source: https://leetcode.com/problems/non-overlapping-intervals/

# import bisect

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Given:
            intervals: A list of intervals ([start, end])
                1 <= len(intervals) <= 1E5          N
                -5E4 <= start_i < end_i <= 5E4
        Return:
            Min. # of intervals to remove to make remaining intervals non-overlapping
            [[1,2],[2,3]] is not overlapping
        
        Obs:
        - There is always a solution (leave 1 interval)

        Bruteforce:
        TIME: O(2^N * N * log N)
        SPACE: O(N)

        Greedy
        DF

        [[1,2], [1,3], [2,3], [3,4]]
        [3, 2, 2, 1]

        Map: i -> Most # of non-overlapping intervals after i

        # TIME: O(N log N)
        # SPACE: O(N)
        # '''
        # MAX_START_TIME = int(5E4+1)
        # N = len(intervals)
        # intervals.sort()
        # max_start = [MAX_START_TIME]  # Integer on starting point of intervals
        # max_from = [0]   # max_from[i] is the largest # of non-overlapping intervals with starting point >= max_start[i]

        # for i in range(N-1, -1, -1):
        #     cur_max = 1 # Max non-overlapping intervals starting with interval `i`
        #     j = bisect.bisect_left(max_start, intervals[i][1])
        #     if max_from[j] + 1 > cur_max:
        #         cur_max = max_from[j] + 1
            
        #     if max_start[0] != intervals[i][0]:
        #         max_start.insert(0, intervals[i][0])
        #         max_from.insert(0, max(cur_max, max_from[0]))
        #     elif max_from[0] < cur_max:
        #         max_from[0] = cur_max 
        
        # return N - max(max_from)

        MIN_END_TIME = int(-5E4)
        intervals.sort(key=lambda pair : (pair[1], pair[0]))
        num_interval = 0
        cur_end = MIN_END_TIME - 1
        for i in range(len(intervals)):
            # Greedily pick amongst possible next interval with earliest end time
            if intervals[i][0] >= cur_end:
                num_interval += 1
                cur_end = intervals[i][1]
        
        return len(intervals) - num_interval
