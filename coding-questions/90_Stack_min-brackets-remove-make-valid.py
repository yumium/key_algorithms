# Source: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def minRemoveToMakeValid(self, s):
    '''
    Given:
        s: input string
            1 <= len(s) <= 1E5
            s[i] is (, ), lower case English letter
    Return:
        s: output string w/ min. parenthesis removed

    Lower case letters matter for output
    Multiple solutions possible
    '''

    # checker -> True/False
    # iterate over all possible removals of brackets, given # of brackets to remove
    # N brackets, O(2^N)
    stack = [] # indices of left brackets => ( 'round', idx )
    removals = [] # Indices of brackets to remove
    for i in range(len(s)):
        if s[i].isalpha():
            continue

        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                removals.append(i)
            else:
                stack.pop()

    res = ""
    for i in range(len(s)):
        if i not in removals and i not in stack:
            res += s[i]

    return res