# Source: https://leetcode.com/problems/kth-missing-positive-number/description/

import bisect

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Given:
            arr: Array of positive integers, sorted in strictly increasing order
                1 <= len(arr) <= 1E4
                1 <= arr[i] <= 1E4
            k: Integer
                1 <= k <= 1000
        Return:
            k-th positive integer missing from array

        Obs:
        - This function always have a unique valid solution

        TIME: O(log N)
        SPACE: O(1)
        '''
        i, j = 0, len(arr)
        # Invariant: # missing until elems in arr[0..i) < k; # missing until elems in arr[j..N) >= k
            # 0 <= i <= j <= N
        while i < j:
            m = (i+j) // 2
            if arr[m] - (m+1) < k:
                i = m+1
            else:
                j = m

        return k + i
