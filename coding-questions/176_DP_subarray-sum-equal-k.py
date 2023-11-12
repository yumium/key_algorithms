# Source: https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Given:
            nums: Array of integers
            k: Integer
                1 <= len(nums) <= 2E4       N
                -1000 <= nums[i] <= 1000

                -1E7 <= k <= 1E7            K
        Return:
            Total # of subarray (contiguous, non-empty) that equal `k` in `nums`

        Bruteforce => try every subarray
        TIME: O(N^2)
        SPACE: O(1)

        Ideas:
        - Subarray a[i:j] = a[:j] - a[:i]
        - Given an integer j, subarray a[i:j] where sum(a[i:j]) = k are all i that satisfy
            sum(a[:j] - a[:i]) = k

        TIME: O(N)
        SPACE: O(N)
        '''
        res = 0
        sums = {0: 1}  # Previous subarray sum from a[0..] => count
        
        j = 0
        cur_sum = 0
        # Invariant: 
        #    `res` is # of subarray in a[:j] that equal k
        #    cur_sum = a[:j]
        #    sums = count of sum(a[:i]) where 0 <= i <= j
        while j < len(nums):
            cur_sum += nums[j]
            
            remain = cur_sum - k
            if remain in sums:
                res += sums[remain]

            if cur_sum in sums:
                sums[cur_sum] += 1
            else:
                sums[cur_sum] = 1

            j += 1

        return res

