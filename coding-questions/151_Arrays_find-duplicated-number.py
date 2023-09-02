# Source: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Given:
            nums: An array of integers, a permutation of [1..n] with another number in [1..n]
                2 <= len(nums) <= 1E5
                1 <= nums[i] <= len(nums)-1
        Return:
            The duplicated number
        
        Ideas:
        - Sort the numbers -> linear scan
        - Use a set

        => no array modification
        => use constant space

        TIME: O(N^2)
        SPACE: O(1)

        1 + ... + n + dup
        '''
        if len(nums) == 2:
            return nums[0]

        head = nums[0]
        slow = nums[head]
        fast = nums[nums[head]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = head
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # return nums.index(slow)
        return slow
