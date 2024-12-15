# Source: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e

def rock_paper_scissors(T, X, W, E):
    '''
    Given:
        T: The number of days to leave instructions
            T = 200
        X: The target average expected rewards over all `T` days
        W: A list of integers representing winning points
        E: A list of integers representing draw points
            len(W) = len(E) = T
            50 <= W <= 950
            0 <= E <= W; E is one of W, W/2, W/10, 0




            on average, W is (5 + 95) / 2 = 500

            So highest of each W, W/2, W/10, 0, when added together, should be at least 14600 * 4 = 58400

            If W is 5, then it's 584 (that's ~50% win points each round)
            
    




    Return:
        A list of string, each string has 60 characters for the strategy of that day
    It is guaranteed that there will be a solution

    Obs:
    - Solutions are not unique
    - Given my strategy for a day, the expected return for that day is deterministic
    - As days are independent, we just need to maximise expected return of each day
    - The exact value of W doesn't matter to get maximum return for a day, as E is always a fraction of W

    - There are essentially 4 scenarios to think about:
        - E is one of W, W/2, W/10, 0
    - If E is higher, we would be less biased to winning
    
    - Bruteforce => for each day try all strategies, and pick the one with highest expected return. Then average expected return will be at least X
    TIME: O(3^60)


    '''


