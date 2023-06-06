# Source: https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        Given:
            brackets: A string of  brackets, ( or ) only
                0 <= len(brackets)
        Return:
            Length of longest valid bracket string
                Valid = all open brackets are closed
            TIME: O(N)
            SPACE: O(N)
        '''
        if len(s) == 0:
            return 0

        longest = 0  # The longest valid substring so far
        start = 0  # The index of the latest segment
        did_break, idx = self.traverse(s, 0)
        print(f'did_break = {did_break}, idx = {idx}')
        while did_break:
            # s[start..idx) is valid
            longest = max(longest, idx-start)
            start = idx+1
            did_break, idx = self.traverse(s, idx+1)
            print(f'did_break = {did_break}, idx = {idx}')
        longest = max(longest, idx)
        return longest
            
    def traverse(self, s, i):
        '''
        Return the first index where there are more ) than (
        Otherwise, return the longest valid substring in s[i:]

        Return tuple (did_break, value)
        '''
        if i == len(s):
            return (False, 0)
        
        if s[i] == '(':
            len_valid = 0
            did_break, idx = self.traverse(s, i+1)
            while did_break:
                len_valid = idx-i+1
                if idx+1 == len(s):
                    return (False, len_valid)
                elif s[idx+1] == ')':
                    return (True, idx+1)
                else:
                    did_break, idx = self.traverse(s, idx+2)
            return (False, max(len_valid, idx))
        
        else:
            return (True, i)

test_string = ')()())'

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses(test_string))


