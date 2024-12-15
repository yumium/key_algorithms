class Solution {
public:
    /*
        Given:
            nums: Integer array
                product(nums) fits into 32-bit integer
                2 <= nums.size() <= 1E5
                -30 <= nums[i] <= 30

        Return:
            answer: integer array s.t. answer[i] = product(nums[j != i])

        Condition:
            Cannot use division

        TIME: O(N)
        SPACE: O(1)
    */
    vector<int> productExceptSelf(vector<int>& nums) {
        const auto N = nums.size();
        vector<int> res (N,1);

        int prefix = nums[0];
        for (int i = 1; i < N; i++) {
            res[i] *= prefix;
            prefix *= nums[i];
        }

        int suffix = nums[N-1];
        for (int i = N-2; i >= 0; i--) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
};