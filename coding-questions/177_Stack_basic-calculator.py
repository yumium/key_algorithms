# Source: https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        '''
        Given:
            s: Evaluation string
                1 <= len(s) <= 3E5
                `s` consists of integers, operators (+-*/) with spaces
                `s` always valid
                All integers >= 0
        Return:
            Value of expression. Note, / does floor division

        Idea:
        - Parsing integers and operators
        - String in form
            - expr = int | int op expr
        - There are no brackets => */ take precedence over +-

        - Parse, then use stack

        TIME: 
        SPACE: 
        '''
        expr = self.parseExpr(s.replace(' ', ''))

        stack = [expr[0]]
        i = 1
        while i < len(expr):
            if expr[i] == '*':
                stack[-1] = stack[-1] * expr[i+1]
            elif expr[i] == '/':
                stack[-1] = stack[-1] // expr[i+1]
            else:
                stack.extend(expr[i:i+2])
            i += 2

        res = stack[0]
        i = 1
        while i < len(stack):
            if stack[i] == '+':
                res += stack[i+1]
            else:
                res -= stack[i+1]
            i += 2
        
        return res

    def parseExpr(self, expr):
        res = []
    
        int_str = ''
        i = 0
        while i < len(expr):
            if expr[i] not in '+-*/':
                int_str += expr[i]
            else:
                res.append(int(int_str))
                int_str = ''
                res.append(expr[i])

            i += 1

        res.append(int(int_str))

        return res


