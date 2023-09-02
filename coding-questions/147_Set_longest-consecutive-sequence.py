# Source: https://leetcode.com/problems/longest-consecutive-sequence/solutions/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Given:
            nums: An array of integers
                0 <= len(nums) <= 1E5
                -1E9 <= nums[i] <= 1E9
        Return:
            The length of the longest consecutive sequence
                (consecutive sequence -> x, x+1, x+2 ...)

        Obs:
        - If len(nums) > 0; return at least 1

        TIME: O(nlogn)
        SPACE: O(1)
        '''
        # if len(nums) == 0:
        #     return 0

        # nums.sort()

        # cur_length = 1
        # longest = 1
        
        # # Invariant: cur_length is the longest consecutive elements sequence ending at index `i`
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         cur_length += 1
        #     elif nums[i] > nums[i-1] + 1:
        #         cur_length = 1
            
        #     longest = max(cur_length, longest)

        # return longest

        nums = set(nums)
        best = 0
        for x in nums:
            if x-1 not in nums:
                y = x  # Invariant: current last element in sequence starting at `x`
                while y+1 in nums:
                    y += 1
                best = max(best, y-x+1)

        return best




