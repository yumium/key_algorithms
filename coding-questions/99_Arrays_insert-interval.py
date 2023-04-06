# Source: https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Given:
            intervals: 
                0 <= len(intervals) <= 1E4
                len(intervals[i]) = 2
                0 <= start <= end <= 1E5
                sorted by start
                intervals non-overlapping => end_i < start_i+1

            newInterval: [start,end]
        Return:
            A list of intervals with newInterval inserted, merging overlapping intervals in necessary
        '''
        minimum, maximum = newInterval[0], newInterval[1]
        res = []

        mode = 'start'
        for left, right in intervals:
            if mode == 'start':
                if right < minimum:
                    res.append([left,right])
                elif left > maximum:
                    res.append([minimum,maximum])
                    res.append([left,right])
                    mode = 'end'
                else:
                    mode = 'merge'
                    minimum = min(minimum, left)
                    maximum = max(maximum, right)
            
            elif mode == 'merge':
                if left > maximum:
                    mode = 'end'
                    res.append([minimum, maximum])
                    res.append([left,right])
                else:
                    minimum = min(minimum, left)
                    maximum = max(maximum, right)
            
            else:
                res.append([left,right])

        if not mode == 'end':
            res.append([minimum, maximum])

        return res

