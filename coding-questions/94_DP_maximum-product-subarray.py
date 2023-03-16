# Source: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maximum = [nums[0]]
        # minimum = [nums[0]]

        # for i in range(1, len(nums)):
        #     maximum.append(max(nums[i], nums[i]*maximum[i-1], nums[i]*minimum[i-1]))
        #     minimum.append(min(nums[i], nums[i]*maximum[i-1], nums[i]*minimum[i-1]))

        # return max(maximum)

        maximum = nums[0]
        minimum = nums[0]

        prev_max, prev_min = maximum, minimum
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i]*prev_max, nums[i]*prev_min)
            cur_min = min(nums[i], nums[i]*prev_max, nums[i]*prev_min)
            maximum = max(maximum, cur_max)
            minimum = min(minimum, cur_min)
            prev_max, prev_min = cur_max, cur_min

        return maximum