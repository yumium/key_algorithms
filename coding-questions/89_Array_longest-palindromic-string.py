# Source: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Given:
            s: input string, only digits and English letters
                1 <= len(s) <= 1000
        Return:
            A longest palindromic substring

        Every singlest string is a palindrome
        '''
        # checker
        # iterate over all substrings of s, from longest to shortest
        # O(N^3) number of substrings of s. 

        # O(N^2)
        

        # odd_l = 0
        # odd_r = 1  # odd_pal = s[odd_l: odd_r]
        odd_longest = ""
        even_longest = ""
        N = len(s)

        # Odd
        for i in range(len(s)): # O(N)
            diff = 1
            while i-diff >= 0 and i+diff < N and s[i-diff] == s[i+diff]:
                diff += 1
            pal = s[i-diff+1: i+diff]
            if len(pal) > len(odd_longest):
                odd_longest = pal

        # Even
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                continue

            diff = 1
            while i-1-diff >= 0 and i+diff < N and s[i-1-diff] == s[i+diff]:
                diff += 1
            pal = s[i-diff: i+diff]
            if len(pal) > len(even_longest):
                even_longest = pal
        
        if len(odd_longest) > len(even_longest):
            return odd_longest
        else:
            return even_longest