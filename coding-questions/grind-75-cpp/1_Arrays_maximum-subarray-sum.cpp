#include <vector>

class Solution {
    public:
        /*
        Given:
            nums: Array of integers, N >= 1

        Return:
            maximum sum of subarray

        Naive = try all subarrays:
        Time: O(N^3)
        Space: O(1)

        Dynamic Programming: maximum ending at i
        Time: O(N)
        Space: O(1)
        */
        int maxSubArray(std::vector<int>& nums) {
            size_t N = nums.size();

            auto current_sum = nums[0];
            auto res = nums[0];

            for (size_t i = 1; i < N; i++) 
            {
                current_sum = std::max(current_sum + nums[i], nums[i]);
                res = std::max(res, current_sum);
            }

            return res;
        }
};