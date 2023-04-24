# Source: https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Given:
            nums: An integer array of unique elements
                1 <= len(nums) <= 10
                -10 <= nums[i] <= 10
        Return:
            A list of all subsets of `nums`
        '''
        if len(nums) == 1:
            return [[], nums]
        else:
            sets = self.subsets(nums[1:])
            return sets + [[nums[0]] + xs for xs in sets]
