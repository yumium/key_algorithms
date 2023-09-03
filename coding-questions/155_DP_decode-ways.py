# Source: https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Given:
            s: A string of numbers
                1 <= len(s) <= 100
        Return:
            The # of different original letter strings that could have resulted in this encoding, can be 0

        3-9 => itself
        1,2 => if next one is:
            _ => itself
            0 => must group
            otherwise => depends if double digit exist

        TIME: O()
        SPACE: O(N)
        '''
        encodingsFrom = [None]*len(s) # encodingsFrom[i] = # of encodings in s[i:]
        return self.numDecodingsMem(s, encodingsFrom)

    def numDecodingsMem(self, s, encodingsFrom):
        if len(s) == 0:
            return 1
        
        if encodingsFrom[-len(s)] is not None:
            return encodingsFrom[-len(s)]

        if s[0] == '0':
            res = 0
        else:
            res = self.numDecodingsMem(s[1:], encodingsFrom)
            if len(s) >= 2 and (s[0] == '1' or (s[0] == '2' and s[1] < '7')):
                res += self.numDecodingsMem(s[2:], encodingsFrom)

        encodingsFrom[-len(s)] = res
        return res

