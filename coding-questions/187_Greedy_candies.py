class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        Given:
            ratings: Array of children ratings      N
                1 <= N <= 2E4
                0 <= ratings[i] <= 2E4
        Return:
            Minimum # of candies you need to satisfy condition

        TIME: O(N)
        SPACE: O(N)

        // --- PROOF OF GREEDY ALGORITHM --- //
        
        I ran out of time to write the full proof, but the key idea is that:
        - Firstly, we can see this algorithm returns a solution that satisfy the conditions
        - Then take any i where candies[i] > 1, then a neighbour must be candies[i]-1. Say the neighbour is candies[i-1] So to decrease candies[i] we need to decrease candies[i], candies[i-1] by same amount. We then realise that this means candies[i-2] needs to decrease by same amount as well (assuming it's not at 1 already). The logic keeps going until candies[0], which is 1 in this case, and hence we cannot decrease at all.
        - This completes the proof by contradition.
        '''
        N = len(ratings)
        if N == 1:
            return 1

        candies = [1]*N     # candies[i] = candies currently allocated to student i
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i], candies[i-1]+1)
        for i in range(N-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                candies[i-1] = max(candies[i-1], candies[i]+1)

        return sum(candies)
