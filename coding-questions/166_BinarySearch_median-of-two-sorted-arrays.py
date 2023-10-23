# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List

class Solution:
    def findMedianSortedArraysLinear(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Given:
            nums1: List of integers, length m, sorted
            nums2: List of integers, length n, sorted
                0 <= m, n <= 1000
                1 <= m + n <= 2000

                -1E6 <= nums1[i], nums2[i] <= 1E6
        Return:
            Median of both arrays
            Have to return in runtime O(log(M+N))

        Obs:
        - Median of odd length is middle number
          Median of even length is average of 2 middle numbers

        Bruteforce:
        TIME: O(K log K)
        SPACE: O(K)
            where K = M + N

        Ideas:
        - 2 pointer => O(K)
        - binary search?

        - 2 kinds: overlap, or non overlap
            - left, mixed, right
        - Median of list themselves

        - Selection? O(N)
        - Find the value of the median
        '''
        i1, j1 = 0, len(nums1)
        i2, j2 = 0, len(nums2)

        for _ in range((len(nums1) + len(nums2) - 1) // 2):
            if i1 == j1 or (i2 < j2 and nums1[i1] > nums2[i2]):
                i2 += 1
            else:
                i1 += 1

            if i1 == j1 or (i2 < j2 and nums1[j1-1] < nums2[j2-1]):
                j2 -= 1
            else:
                j1 -= 1
        
        remaining = nums1[i1:j1] + nums2[i2:j2]
        return sum(remaining) / len(remaining)


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass




