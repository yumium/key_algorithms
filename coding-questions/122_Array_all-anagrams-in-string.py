# Source: https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Given:
            s, p: String of lowercase English letters
                1 <= len(s), len(p) <= 3E4
        Return:
            A list of indices of s where it's the beginning of p's anagram

        Obs:
        - len(p) > len(s), return []
        '''

        # TIME: O(N)
        # SPACE: O(M)

        if len(p) > len(s):
            return []
        
        M = len(p)
        N = len(s)
        ORD = 97
        res = []
        count = [0]*26
        target = [0]*26

        for x in s[:M]:
            count[ord(x)-ORD] += 1
        for x in p:
            target[ord(x)-ORD] += 1
        
        if self.is_eq_array(count, target):
            res.append(0)

        for i in range(1, N-M+1):
            count[ord(s[i-1])-ORD] -= 1
            count[ord(s[i+M-1])-ORD] += 1
            if self.is_eq_array(count, target):
                res.append(i)

        return res
        
    def is_eq_array(self, xs, ys):
        if len(xs) != len(ys):
            return False

        for i in range(len(xs)):
            if xs[i] != ys[i]:
                return False
        return True
