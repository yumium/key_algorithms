import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        Given:
            nums1: Integer array
            nums2: Integer array
            k: # of pairs to return
                nums1, nums2 sorted in non-decreasing order
                1 <= len(nums1), len(nums2) <= 1E5      N = max(N1, N2)
                -1E9 <= nums1[i], nums2[i] <= 1E9
                1 <= k <= 1E4
        Return:
            List of k pairs with smallest sums. Return in non-decreasing order of sum. If k > N1*N2, return all pairs.

        Ideas/Obs:
        - # of pairs is N1 * N2, it's possible that k > N1 * N2 where we'll return all pairs

        Bruteforce => check all pairs, sort, return smallest k
        TIME: O(N^2 log N^2)
        SPACE: O(N^2)

        This algo:
        TIME: O(K * log(N))
        SPACE: O(N)
        '''
        MAX_PAIR_SUM = int(1E9 * 2 + 1)
        N1 = len(nums1)
        N2 = len(nums2)
        next_from_nums2 = [0]*N1        # next pair for nums1[i] is (nums1[i], nums2[next_from_nums2[i]])
        res = []

        candidates = [((nums1[i]+nums2[0]), i) for i in range(N1)] # (next pair sum using nums1[i], i), or (MAX_INTEGER, i) if all pairs of (nums1[i], _) are in res
        while len(res) < min(N1 * N2, k):
            next_sum, idx_num1 = heapq.heappop(candidates)
            idx_num2 = next_from_nums2[idx_num1]
            res.append([nums1[idx_num1], nums2[idx_num2]])
            if idx_num2 == N2-1:
                heapq.heappush(candidates, (MAX_PAIR_SUM, idx_num1))
            else:
                next_from_nums2[idx_num1] += 1
                heapq.heappush(candidates, (nums1[idx_num1] + nums2[idx_num2+1], idx_num1))

        return res
