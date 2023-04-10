# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(self, s: str) -> int:
    '''
    Given:
        s: A string
            0 <= len(s) <= 5E4
            Consist of English letters, digits, symbols and spaces
    Return:
        An integer -> longest substring without repeating characters
    '''

    # TIME: O(N)
    # SPACE: O(N)

    seen = {}  # chr -> idx
    longest = 0
    l = i = 0

    # Invariant: 0 <= l <= i < len(s); s[l..i] is the longest unique substring ending at index i-1
    while i < len(s):
        chr = s[i]
        if chr in seen:
            l = max(seen[chr]+1,l)
        seen[chr] = i
        longest = max(longest, i-l+1)
        i += 1

    return longest