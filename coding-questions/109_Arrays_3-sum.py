# Source: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Given:
            nums: A list of numbers
                3 <= len(nums) <= 3000
                -1E5 <= nums[i] <= 1E5
        Return:
            A list of triples (as lists) that are elements in the list which sums up to 0. Cannot return duplicates
        '''
        res = set()  # Triples
        nums.sort()

        # Check triples starting with element nums[i]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            # Invariant: The rest of triples are in range nums[l..r]
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return [list(xs) for xs in res]

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        '''
        Given:
            nums: A list of numbers
                3 <= len(nums) <= 3000
                -1E5 <= nums[i] <= 1E5
        Return:
            A list of triples (as lists) that are elements in the list which sums up to 0. Cannot return duplicates
        '''
        res = set()  # Triples

        for i in range(len(nums)):
            target = -nums[i]

            seen = set()
            for j in range(len(nums)):
                if j == i:
                    continue

                if len(seen) > 0 and target-nums[j] in seen:
                    res.add(tuple(sorted([nums[i], nums[j], target-nums[j]])))
                seen.add(nums[j])
        
        return [list(xs) for xs in res]