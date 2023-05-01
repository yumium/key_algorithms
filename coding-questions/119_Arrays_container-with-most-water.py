# Source: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Given:
            height: heights of tubes
                2 <= len(height) <= 1E5
                0 <= height[i] <= 1E4
        Return:
            Maximum amount of water a container can store

        Obs:
        - Volume(i, j) = (j-i) * min(height[i], height[j])

        Explanation:
        - We can start w/ the widest possible container
        - Then next step the other candidates must be a container of smaller size within this container's width
        - We can safely remove the bar that is smaller in the 2 bars, because if a candidate uses the smaller bar, the height of container cannot be bigger, yet the width will be smaller, giving an inferior result
        - And we recurse like so ...
        '''
        max_vol = -1
        i, j = 0, len(height)-1
        while i < j:
            max_vol = max(max_vol, (j-i) * min(height[i], height[j]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        
        return max_vol
