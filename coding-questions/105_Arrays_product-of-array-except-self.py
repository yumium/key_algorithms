# Source: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Given:
            nums: integer array
                2 <= len(nums) <= 1E5
                -30 <= nums[i] <= 30
        Return:
            answer: integer array, answer[i] is product of nums apart from nums[i]
                Guaranteed to be in 32-bit integer
        '''

        res = [1]*len(nums)

        accum = 1
        for i in range(len(nums)-1):
            accum *= nums[i]
            res[i+1] *= accum
        
        accum = 1
        for i in range(len(nums)-1, 0, -1):
            accum *= nums[i]
            res[i-1] *= accum

        return res
