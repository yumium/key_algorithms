https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        Given:
            citations: Array of # citations received for each paper
                1 <= len(citations) <= 5E4      N
                0 <= citations[i] <= 1E4        K
        Return:
            Researcher's h-index
            h-index is the maximum value of h s.t. researcher has published at least h papers each with at least h citations

        Bruteforce: Try h-index in increasing value of h, stop until it's no longer valid
        TIME: O(N*K)
        SPACE: O(1)

        Better: use binary search
        Obs:
        - h-index of 0 is always valid
        - 0 <= h-index <= len(citations)

        TIME: O(N log N)
        SPACE: O(1)
        '''
        i, j = 0, len(citations)+1
        # Invariant: [0..i) are valid h-index; [j..N+1) are invalid h-index; 0 <= i <= j <= N+1
        while i < j:
            m = (i+j) // 2
            if self.isValidHIndex(citations, m):
                i = m+1
            else:
                j = m
        
        # 0 < i = j <= N+1
        return i-1

    def isValidHIndex(self, citations, h):
        return len([cit for cit in citations if cit >= h]) >= h
