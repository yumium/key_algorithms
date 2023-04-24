# Source: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        Given:
            nums: An array of integers
                1 <= len(nums) <= 200
                1 <= nums[i] <= 100
        Return:
            Whether you can partition the array into 2 subsets s.t. sum of the 2 subsets are equal
            
        Obs:
        - sum(nums) is odd => return False
        - sum(subset(nums)) = sum(nums) / 2    <->   canPartition

        - Binary search idea
        '''
        total = sum(nums)
        if total%2 == 1:
            return False

        target = total // 2

        grid = [None]*(len(nums)+1)
        for i in range(len(grid)):
            grid[i] = [0]*(target + 1)

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if nums[i-1] > j:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = max(grid[i-1][j], nums[i-1] + grid[i-1][j-nums[i-1]])
        
        return grid[-1][-1] == target
    
    def canPartition2(self, nums: List[int]) -> bool:
        '''
        Given:
            nums: An array of integers
                1 <= len(nums) <= 200
                1 <= nums[i] <= 100
        Return:
            Whether you can partition the array into 2 subsets s.t. sum of the 2 subsets are equal
            
        Obs:
        - sum(nums) is odd => return False
        - sum(subset(nums)) = sum(nums) / 2    <->   canPartition

        - Binary search idea
        '''
        total = sum(nums)
        if total%2 == 1:
            return False

        target = total // 2

        sums = set()
        for n in nums:
            new_sums = {n+m for m in sums}
            new_sums.add(n)
            sums |= new_sums  # All sums of subsets in nums up to and including `n`
            if target in sums:
                return True

        return False