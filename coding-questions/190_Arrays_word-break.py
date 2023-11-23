# Source: https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        Given:
            s: A string
            wordDict: A list of words in the dictionary
                1 <= len(s) <= 20               S
                1 <= len(wordDict) <= 1000      N
                l <= len(wordDict[i]) <= 10     W

                All consist only of lowercase English letters
                All words in `wordDict` are unique
                len(ANS) <= 1E5
        Return:
            All possible ways to add spaces to `s` s.t. every word is in `wordDict`
            The word in `wordDict` can be used multiple times

        Bruteforce => O((S+1)!)

        Obs/Idea:
        - Recursive?
            - Keep increasing prefix as long as it's a prefix of a word
            - Recurse in when the prefix is a word
            - Stop when the prefix is not a prefix of any word

        TIME: O(N*W) + O(S^2 * R)
        SPACE: O(N*W) + O(S^2 * R)
        '''
        cacheWordBreak = {}
        return self.wordBreakRecurse(s, wordDict, cacheWordBreak)

    def wordBreakRecurse(self, s, wordDict, cacheWordBreak):
        N = len(s)
        res = []
        for word in wordDict:
            if s.startswith(word):
                if len(s) == len(word):
                    res.append(s)
                else:
                    j = len(word)
                    if s[j:] in cacheWordBreak:
                        split_postfix = cacheWordBreak[s[j:]]
                    else:
                        split_postfix = self.wordBreakRecurse(s[j:], wordDict, cacheWordBreak)
                    if len(split_postfix) > 0:
                        res.extend([word + ' ' + postfix for postfix in split_postfix])    
        cacheWordBreak[s] = res
        return res

