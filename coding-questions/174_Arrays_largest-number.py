# Source: https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        Given:
            nums: List of non-negative integers
                1 <= len(nums) <= 100
                0 <= nums[i] <= 1E9
        Return:
            Arrange so it form the largest number, return as string
            Answer should be concatenation of 
        
        Bruteforce:

        Obs:
        - Number can be compared lexicographically
        - Self pad with first digit then order by reverse lexicographic order
            - First digit is larger first, within same first digit, recurse lexicographically, no digit left is preferred for < previous digit

        36, 365 => 33331 or 33133

        AAB
        ABA

        33
        30
        34
        55
        99

        TIME: O(N log N)
        SPACE: O(N)

        - First round we compare first digit, and sort reverse order
        - Within each partition (xy)
            - In order, xy | x => xxy, xyx
                63637, 63
    
        Sort with comparison function

        x >= y iff str(x)+str(y) >= str(y)+str(x)
        x = y iff str(x)+str(y) == str(y)+str(x)

        RAT

        T:
        x > y & y > z => x > z
        str(x)+str(y) > str(y)+str(x)
        str(y)+str(z) > str(z)+str(y)

        str(x)+str(z) > str(z)+str(x)

        '''
        # nums_str = [str(x) for x in nums]
        # max_len = max(len(n) for n in nums_str)
        
        # # Pad number string
        # nums_str = [x + x[0] * (max_len - len(x)) for x in nums_str]
        # nums_str = [(x,i) for i, x in enumerate(nums_str)]
        # nums_str.sort(reverse=True)

        # res = ''
        # for _, i in nums_str:
        #     res += str(nums[i])
        
        # return res

        class LexiKey(str):
            def __lt__(x, y):
                return x+y > y+x
        
        ans = ''.join(sorted([str(n) for n in nums], key=LexiKey))
        return '0' if ans[0] == '0' else ans
