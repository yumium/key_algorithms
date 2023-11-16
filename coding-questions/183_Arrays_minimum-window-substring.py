# Source: https://leetcode.com/problems/minimum-window-substring/solutions/

from collections import Counter

class Bag:
    def __init__(self, values):
        self.bag = dict(Counter(values))

    def add(self, val):
        if val in self.bag:
            self.bag[val] += 1
        else:
            self.bag[val] = 1

    def remove(self, val):
        if val in self.bag:
            self.bag[val] -= 1
        else:
            self.bag[val] = -1

    def isNonpositive(self):
        return all([v <= 0 for v in self.bag.values()])

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Given:
            s: A string of English letters          M
            t: Target string of English letters     N
                1 <= M, N <= 1E5
        Return:
            Minimum window substring of `s` s.t. every character in `t` (incl. duplicates) exists in the substring.
            Return "" if no such substring exist

        Bruteforce => try every substring
        TIME: O(M)
        SPACE: O(N)

        Obs:
        - 2 pointer?
        '''
        bestStart = bestEnd = None      # s[bestStart..bestEnd] is the current minimum window substring
        l = r = 0
        targetDiff = Bag(t)
        targetDiff.remove(s[0])         # bag(t) - bag(s[l..r])

        finished = False
        # Invariant: 0 <= l <= r < M
        while not finished:
            if targetDiff.isNonpositive():
                if bestStart is None or r-l < bestEnd-bestStart:
                    bestStart = l
                    bestEnd = r
                l += 1
                targetDiff.add(s[l-1])
                if l > r:
                    r += 1
                    if r == len(s):
                        finished = True
                    else:
                        targetDiff.remove(s[r])
            else:
                r += 1
                if r == len(s):
                    finished = True
                else:
                    targetDiff.remove(s[r])
        
        if bestStart is not None:
            return s[bestStart:bestEnd+1]
        else:
            return ""
