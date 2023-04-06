# Source: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Given:
            nums: An integer array
                len(nums) >= 1
                -1E4 <= nums[i] <= 1E4
        Return:
            sum of the larget subarray
        '''

        cur_max = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            cur_max = max(cur_max, nums[i])
        return cur_max
