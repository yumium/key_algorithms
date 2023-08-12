# Source: https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a709

from math import factorial

def expected_score_naive(N):
    '''
    Given:
        N: The # of cards in the pile at the start
            1 <= N <= 10, 1E6, 1E18
    Return:
        The expected score of the game

    Examples:
    - N = 1
        1, as we always take first card
    - N = 2
        1.5, as if it's [1,2] we take both cards, and if it's [2,1] we take first card

    Obs:
    - The game ends exactly after N rounds
    - The sequence of cards checked is a permutation of [1..N], each permutation has equal probability of occuring
    - Value of each game is at least 1 (taking first card)

    Bruteforce:
    1. Enumerate all permutations of [1..N]
    2. Check value for each permutation
    3. Return average value

    TIME: O(N * N!)
    SPACE: O(N)
    '''
    ps = perms(list(range(1,N+1)))
    total = 0  # Total value in all games

    for p in ps:
        total += value(p)

    return total / factorial(N)


def perms(arr):
    '''Return an iterator for all permutations of `arr`'''
    if len(arr) == 1:
        yield arr
    else:
        for i in range(len(arr)):
            for p in perms(arr[:i] + arr[i+1:]):
                yield [arr[i]] + p


def value(p):
    '''Given a list of cards drawn, return the value of the game'''
    total = 1  # Value of this game, initially with value from first card

    for i in range(1, len(p)):
        if p[i] > p[i-1]:
            total += 1
    
    return total


def expected_score(N):
    '''
    Given:
        N: The # of cards in the pile at the start
            1 <= N <= 10, 1E6, 1E18
    Return:
        The expected score of the game

    TIME: O(N)
    SPACE: O(1)
    '''
    n = 1
    k = 1

    # Invariant: `k` is the expected score for a game with `n` cards
    while n < N:
        n += 1
        k = (1/n) * k + (1/n) * (k+1) + ((n-2)/n) * (k + 1/(n-1))
    
    return k

INPUT = './input-easy.txt'

# if __name__ == '__main__':
#     with open(INPUT, 'r') as f:
#         t = int(f.readline().strip())
#         for i in range(1, t+1):
#             N = int(f.readline().strip())
#             ans = expected_score_naive(N)
#             print(ans)



