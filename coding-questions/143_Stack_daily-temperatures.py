class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Given:
            temperatures: An array of integers
                1 <= len(temperatures) <= 1E5
                30 <= temperatures[i] <= 100
        Return:
            answer: An array that is the number of days you have to wait after the ith day to get a warmer temperature. 0 if never warmer

        Obs:
        - Last element of answer is always 0
        - [(71, 3)]

        Bruteforce:
        TIME: O(N^2)
        SPACE: O(1)

        New:
        TIME: O(N)
        SPACE: O(N)
        '''
        res = [0] * len(temperatures)
        stack = [] # A stack of unresolved days, in format (temperature, index), temperature must be monotonically decreasing in stack

        for i in range(len(temperatures)):
            # Resolve days
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((temperatures[i], i))

        return res