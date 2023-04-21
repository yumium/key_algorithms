# Source: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        Given:
            nums: A list of numbers
                1 <= len(nums) <= 6
                -10 <= nums[i] <= 10
                all numbers in nums distinct
        Return:
            A list of all permutations of `nums`
        '''
        if len(nums) == 1:
            return [nums]

        res = []
        for xs in self.permute(nums[1:]):
            for i in range(len(nums)):
                res.append(xs[:i] + [nums[0]] + xs[i:])
        return res