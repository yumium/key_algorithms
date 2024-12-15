using namespace std;

class Solution {
public:
    /*
        Given:
            nums: Integer array of numbers
                3 <= nums.size() = N <= 3000
                -1E5 <= nums[i] <= 1E5
        
        Return:
            set of triplets that sum up to 0, must not repeat

        SODSBUDA

        Idea 1: 3sum => 2sum
        Time: O(N^2)
        Space: O(N)

        Obs:
        - 2sum => O(N)
        - The sum 0 is arbitrary
        - i => 0-i 
            - sort numbers
            - x
        - Sorting?
    */
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res {};
        const int N = nums.size();

        for (size_t i = 0; i < N-2; i++) {
            const int target = 0 - nums[i];
            set<int> prev {};

            for (size_t j = i+1; j < N; j++) {
                const int val = nums[j];

                if (prev.find(target-val) != prev.end()) {
                    vector<int> input {-target, val, target-val};
                    std::sort(input.begin(), input.end(), greater<int>());
                    res.insert(input);
                }
                prev.insert(val);
            }
        }

        vector<vector<int>> out {};
        for (auto& triple: res) {
            out.push_back(triple);
        }
        
        return out;
    }
};
