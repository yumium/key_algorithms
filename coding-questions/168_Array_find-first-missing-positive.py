# Source: https://leetcode.com/problems/first-missing-positive/

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Given:
            nums: Unsorted integer array
                1 <= len(nums) <= 1E5
                nums[i] is a 32-bit integer
                Integers can be duplicated
        Return:
            Smallest missing positive integer (>= 1)

        Target:
        TIME: O(N)
        SPACE: O(1)

        Bruteforce: Sort then one pass
        TIME: O(N log N)
        SPACE: O(1)

        Ideas: 
        - Store numbers in set (?)
        - Modify original array?

        Obs:
        - 1 <= ans <= len(nums) + 1
        '''
        if 1 not in nums:
            return 1
        
        N = len(nums)
        for i in range(N):
            if nums[i] < 1:
                nums[i] = 1  # This does not affect the answer

        # nums[0..i] have marked their respective values
        for i in range(N):
            if 1 <= abs(nums[i]) <= N:
                nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1])
        
        for i in range(N):
            if nums[i] > 0:
                return i+1

        return N+1


if __name__ == '__main__':
    sol = Solution()

    print(sol.firstMissingPositive([1,2,0]))
    print(sol.firstMissingPositive([3,4,-1,1]))
    print(sol.firstMissingPositive([7,8,9,11,12]))