# Source: https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Given:
            asteroids: An array of integers
                Abs value = size; Sign = direction (neg = left, pos = right)
                Asteroids move in same speed

                2 <= len(asteroids) <= 1E4
                -1E4 <= asteroids[i] <= 1E4, never 0
        Return:
            State of asteroid after all collisions

        Obs:
        - Collision -> only with adjacent numbers with sign [pos, neg]

        Bruteforce:
        TIME: O(N * N)
        SPACE: O(N)

        Assume order doesn't matter (prove that resolution order is not ambiguous)
        => greedily resolve left most conflict

        TIME: O(N^2)
        SPACE: O(1)
        '''
        i = 0
        # Variant: (N-i) + N, where N = current length of `asteroids`
        while i+1 < len(asteroids):
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if asteroids[i] > -asteroids[i+1]:
                    asteroids.pop(i+1)
                elif asteroids[i] < -asteroids[i+1]:
                    asteroids.pop(i)
                else:
                    asteroids.pop(i)
                    asteroids.pop(i)
                i = max(i-1, 0)
            else:
                i += 1
        
        return asteroids

        # Solution without shifting arrays
        # N = len(asteroids)
        # left = []
        # i = 0
        # # Invariant: Current asteroid state is  left ++ asteroids[i:N) & left most element to check is asteroids[i]
        # while i+1 < N:
        #     if asteroids[i] > 0 and asteroids[i+1] < 0:
        #         if asteroids[i] > -asteroids[i+1]:
        #             asteroids[i+1] = asteroids[i]
        #             i += 1
        #         elif asteroids[i] < -asteroids[i+1]:
        #             i += 1
        #         else:
        #             i += 2

        #         if len(left) > 0:
        #             asteroids[i-1] = left.pop()
        #             i -= 1
        #     else:
        #         left.append(asteroids[i])
        #         i += 1
        
        # return left + asteroids[i:]
