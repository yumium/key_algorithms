# Source: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

from collections import Counter

class Bag:
    def __init__(self, items):
        self.count = dict(Counter(items))
        self.zeros = 0

    def is_empty(self):
        return self.zeros == len(self.count)

    def add(self, item):
        if item not in self.count:
            self.count[item] = 1
        elif self.count[item] == -1:
            self.count[item] = 0
            self.zeros += 1
        elif self.count[item] == 0:
            self.count[item] = 1
            self.zeros -= 1
        else:
            self.count[item] += 1

    def remove(self, item):
        if item not in self.count:
            self.count[item] = -1
        elif self.count[item] == 1:
            self.count[item] = 0
            self.zeros += 1
        elif self.count[item] == 0:
            self.count[item] = -1
            self.zeros -= 1
        else:
            self.count[item] -= 1

    def __eq__(self, other):
        return self.count == other.count

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        Given:
            s: A string
            words: List of words of equal length
                1 <= len(s) <= 1E4              N
                1 <= len(words) <= 5E3          W
                1 <= len(word[i]) <= 30         K
                All lowercase English letters
        Return:
            A list of starting indices where it is a concatenated substring

        Obs:
        - No solution len(words) * len(words[i]) > len(s)

        Bruteforce => checking all index
        TIME: O(M * (N*K + N))
        SPACE: O(N)

        Ideas:
        - wordgoodgoodgood => goodgoodgoodbest
            This only requires removing 'word' and adding 'best'
        - Assuming Bag exists as a data structure
        - TIME: O(N*K)
        - SPACE: O(W)
        '''
        N = len(s)
        W = len(words)
        K = len(words[0])
        res = []

        if W * K > N:
            return []

        for l in range(K):
            if l + W * K > N:
                break

            words_diff = Bag(words)   # 
            for i in range(l, l+W*K, K):
                words_diff.remove(s[i:i+K])

            if words_diff.is_empty():
                res.append(l)
    
            while l + (W+1) * K <= N:
                words_diff.add(s[l:l+K])
                words_diff.remove(s[l+W*K : l+(W+1)*K])
                l += K
                if words_diff.is_empty():
                    res.append(l)
        
        return res
    
