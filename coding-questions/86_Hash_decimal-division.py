# Source: https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def sign(self, num):
        if num >= 0:
            return 1
        else:
            return -1

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        Given:
            numerator: Int, 
            denominator: Int
            -2^31 <= numerator, denominator <= 2^31 - 1 (32-bit integer)
        Return:
            fraction in string, use parenthesis for repeating decimals
            len(answer) < 1E4
        '''
        assert(denominator != 0)

        sign_str = "-" if self.sign(numerator)*self.sign(denominator) < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = numerator // denominator
        remainder = numerator % denominator
        remainders = {remainder: 0}

        if remainder == 0:
            if quotient == 0:
                return str(quotient)
            else:
                return sign_str + str(quotient)

        decimal = str((remainder*10) // denominator)
        cur_remainder = (remainder*10) % denominator
        
        # Invariant:
        #   `remainders` is history of remainders before `cur_remainder`, mapped to its position
        #   `decimal` is string of decimals before `cur_remainder`
        #   `cur_remainder` is the current remainder
        while cur_remainder != 0 and cur_remainder not in remainders:
            decimal += str((cur_remainder*10) // denominator)
            remainders[cur_remainder] = len(remainders)
            cur_remainder = (cur_remainder*10) % denominator

        if cur_remainder == 0:
            return sign_str + str(quotient) + "." + decimal
        else:
            i = remainders[cur_remainder]
            return sign_str + str(quotient) + "." + decimal[:i] + "(" + decimal[i:] + ")"


