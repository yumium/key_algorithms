# Source: https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Given:
            nums: A list of numbers (elements are in list [0,1,2])
                1 <= len(nums) <= 300
        Return:
            Nothing, sort the numbers in-place

        TIME: O(NlogN) on average
        SPACE: O(1)

        Bucketsort:
        TIME: O(N)
        SPACE: O(1)
        """
        buckets = [0]*3

        for n in nums:
            buckets[n] += 1
        
        j = 0
        for i in range(len(nums)):
            while buckets[j] == 0:
                j += 1
            nums[i] = j
            buckets[j] -= 1
