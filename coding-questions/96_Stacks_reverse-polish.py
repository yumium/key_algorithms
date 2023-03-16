# Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = j = 0
        
        # Invariant: stack = tokens[0..i); remaining = tokens[j..N)
        while j < len(tokens):
            if tokens[j] in "+-*/":
                res = int(eval(tokens[i-2] + tokens[j] + tokens[i-1]))
                tokens[i-2] = str(res)
                i -= 1
            else:
                tokens[i] = tokens[j]
                i += 1
            j += 1
        
        return int(tokens[i-1])

