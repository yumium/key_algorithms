# Source: https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        Given:
            nums: Array of distinct positive integers
                1 <= len(nums) <= 200       N
                1 <= nums[i] <= 1000        K
            target: Target integer
                1 <= target <= 1000
        Return:
            # of possible combinations of numbers in `nums` that add up to `target`
            Note, numbers can be used more than once, difference sequences are counted as different combinations

        Bruteforce:
        - Try all combinations -> up to K numbers
            TIME: O(N^K)
            SPACE: O(N^K)
        
        Obs:
        
        [1, 1, 2, 4, 7]

        Ideas:
        - DP?
            - C(t) = sum{C(t-i) | i in nums, i <= t}

        TIME: O(N*K)
        SPACE: O(N)

        O(N*K) possible
        '''
        numToSum = [0]*(target+1)   # Total # of number sequence that add up to i
        numToSum[0] = 1

        for t in range(1, target+1):
            numToSum[t] = sum([numToSum[t-n] for n in nums if n <= t])
        
        return numToSum[target]

