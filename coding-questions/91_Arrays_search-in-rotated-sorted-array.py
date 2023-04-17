# Source: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Given:
            nums: Array of sorted array rotated at unknown pivot index k; 0 <= k < len(nums)
                1 <= len(nums) <= 5000
                All values of nums are unique
                -1E4 <= nums.val <= 1E4
            target: a number, -1E4 <= target <= 1E4
        Return:
            index of `target` in `nums`, or -1 if not in `nums`
        
        
        Bijective function between indices of sorted array and new array
        Unique value = strictly increasing
        '''
        N = len(nums)

        # Invariant: nums[0..i) >= head; nums[j..N) < head
        head = nums[0]
        i, j = 0, N
        while i < j: # TODO: check that i cannot be larger than j
            m = (i+j) // 2
            if nums[m] >= head:
                i = m+1
            else:
                j = m
        offset = j

        # Invariant: nums[0..i) < target; nums[j..N) >= target
        i, j = 0, N
        while i < j:
            m = (i+j) // 2
            if nums[(m+offset)%N] < target:
                i = m+1
            else:
                j = m
        
        if i == N or nums[(j+offset)%N] != target:
            return -1
        else:
            return (j+offset)%N