# Source: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e

from math import ceil

MODULO = int(1E9 + 7)

def smaller_strings(K, S, N):
    '''
    Given:
        K: The # of first letter that can be used
            1 <= K <= 26
        S: A string of length `N`
        N: The length of string `S`
            1 <= N <= 1E5
    Return:
        The number of palindromic strings of length N, smaller than S, and consist of only first K letters of the English alphabet
            Note, these strings don't have to be English words

    Examples:
    - N = 2; K = 3; S = bc
        aa, bb => 2
    - N = 5; K = 5; S = abcdd
        aaaaa, aabaa, aacaa, aadaa, aaeaa, ababa, abbba, abcba
    
    TIME: O(K^N * N)
    SPACE: O(N)

    Obs:
    - If we have an index where the palindrome is strictly smaller, then the rest of the characters don't have restrictions

    TIME: O(N log N)
    SPACE: O(1)
    '''
    return int(smaller_strings_iter(K, S, N, S))

def smaller_strings_recur(K, S, N, S_orig):
    '''
        Returns # of palindromic strings of length N, smaller than S, consist of only first K letters of the English alphabet, and take prefix of S_orig until its end
    '''
    res = (ord(S[0]) - ord('a')) * exponential_modulo(K, ceil(len(S) / 2) - 1, MODULO)

    if len(S) <= 2:
       addition = 1 if is_largest_palindrome_smaller(S_orig) else 0
       return (res + addition) % MODULO
    else:
        return (res + smaller_strings_recur(K, S[1:len(S)-1], N, S_orig)) % MODULO

def smaller_strings_iter(K, S, N, S_orig):
    '''
        Returns # of palindromic strings of length N, smaller than S, consist of only first K letters of the English alphabet, and take prefix of S_orig until its end
        Let's avoid tail recursion
    '''
    res = (ord(S[0]) - ord('a')) * exponential_modulo(K, ceil(len(S) / 2) - 1, MODULO)

    while len(S) > 2:
        S = S[1:len(S)-1]
        res = (res + (ord(S[0]) - ord('a')) * exponential_modulo(K, ceil(len(S) / 2) - 1, MODULO)) % MODULO
    
    addition = 1 if is_largest_palindrome_smaller(S_orig) else 0
    return (res + addition) % MODULO


def is_largest_palindrome_smaller(S):
    '''
        Returns if S[:ceil(len(S)/2)] + reverse(S[:floor(len(S)/2)]) is smaller lexicographically than S
    '''
    assert len(S) > 0

    for i in range(ceil(len(S) / 2), len(S)):
        j = None
        if len(S)%2 == 0:
            j = len(S)//2 - ((i - len(S)//2) + 1)
        else:
            j = len(S)//2 - (i - (len(S)//2))

        if S[j] < S[i]:
            return True
        elif S[j] > S[i]:
            return False
    
    return False

def exponential_modulo(base, exponent, modulo):
    '''
        Returns (base ** exponent) % modulo
        TIME: O(log(exponent))
    '''
    if exponent == 0:
        return 1

    base = base % modulo
    extra = 1

    # Invariant: (base_orig ** exponent_orig) % modulo = (base ** exponent) * extra
    # base < modulo
    # extra < modulo 
    while exponent > 1:
        if exponent%2 == 0:
            base = (base * base) % modulo
            exponent = exponent // 2
        else:
            extra = (extra * base) % modulo
            exponent = exponent - 1
    
    return (base * extra) % modulo

INPUT = './input-hard.txt'
ANS = './ans-hard.txt'
SKIPPED = []

if __name__ == '__main__':
    incorrect = []

    with open(INPUT, 'r') as f:
        with open(ANS, 'r') as g:
            t = int(f.readline().strip())
            for i in range(1, t+1):
                if i in SKIPPED:
                    f.readline()
                    f.readline()
                    g.readline()
                else:
                    [N, K] = [int(x) for x in f.readline().strip().split(' ')]
                    S = f.readline().strip()
                    ans = smaller_strings(K, S, N)
                    ans_string = f"Case #{i}: {ans}"
                    correct_string = g.readline().strip()
                    print(ans_string)
                    assert ans_string == correct_string, ans_string + ", " + correct_string + ", " + ", ".join([str(x) for x in [N, len(S), K]])

