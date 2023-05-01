# Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Given:
            digits: A string of digits
                0 <= len(digits) <= 4
                2 <= digits[i] <= 9
        Return:
            A list of all letter combinations the digits can represent
        '''

        # TIME: O(4^N)
        # SPACE: O(1)

        if len(digits) == 0:
            return []

        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        if len(digits) == 1:
            return [l for l in letters[int(digits[0])]]

        res = []
        suffix = self.letterCombinations(digits[1:])
        for l in letters[int(digits[0])]:
            res.extend([l+ls for ls in suffix])
        
        return res
