# Source: https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Given:
            s: A string of lowercase English letters
                1 <= len(s) <= 300
            wordDict: A list of words
                1 <= len(wordDict) <= 1000
                1 <= len(wordDict[i]) <= 20
                all words unique
        Return:
            True or False that this string can be a sequence of words in `wordDict`

        Obs:
        - There can be more than 1 way to separate s into sequence of words (e.g., s = 'aaa', wordDict = ['a', 'aa'])
        
        TIME: O(W*N)
        SPACE: O(W)
        '''
        canBreak = [False] * len(s)

        for i in range(len(s)-1, -1, -1):
            # Checking s[i:]
            for word in wordDict:
                if s[i:].startswith(word) and (s[i:] == word or canBreak[-(len(s)-i-len(word))]):
                    canBreak[-(len(s)-i)] = True
        
        return canBreak[0]
