# Source: 
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        '''
        Given:
            nums: A list of integer arrays sorted in non-decreasing order
                1 <= len(nums) <= 3500          N
                1 <= len(nums[i]) <= 50         K
                -1E5 <= nums[i][j] <= 1E5
        Return:
            Smallest range ([x,y]) that include at least 1 number from each list
            Size of range break ties with value of x

        Bruteforce: Try every possible range
        TIME: O((N*K)^2)
        SPACE: O(1)

        Obs:
        - There is always a valid range -> there's a valid min. range

        Ideas:
        
        Necessary conditions
        - Starting point <= all max
        - Ending point >= all min

        Given a starting point, ending point is max of min in each list that is >= starting point

        Optimisations:
        - Can check possible ending points if there are fewer to check
        - Any way to prune starting points?

        TIME: O(N^2*K)
        SPACE: O(N*K)
        '''
        N = len(nums)
        start = min([max(arr) for arr in nums])
        candidates = set()
        for arr in nums:
            for num in arr:
                if num <= start:
                    candidates.add(num)
        candidates = sorted(list(candidates), reverse=True)

        # Invariant: best_start <= best_end; it is a valid range
        best_start = min([min(arr) for arr in nums])
        best_end = max([max(arr) for arr in nums])

        # Invariant: indices are valid for current candidate
        indices = [len(arr)-1 for arr in nums]

        for c in candidates:
            for i in range(N):
                j = indices[i]
                while j > 0 and nums[i][j-1] >= c:
                    j -= 1
                indices[i] = j
            candidate_end = max(nums[x][indices[x]] for x in range(N))

            if (candidate_end - c) < (best_end - best_start) or ((candidate_end - c) == (best_end - best_start) and c < best_start):
                best_start = c
                best_end = candidate_end
        
        return [best_start, best_end]

if __name__ == '__main__':
    sol = Solution()

    print(sol.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
    print(sol.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))

