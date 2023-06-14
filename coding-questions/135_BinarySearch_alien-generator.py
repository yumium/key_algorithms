# Source: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb

from math import ceil, sqrt

def num_gold_bars_orig(G):
    '''
    Given:
        G: Max # of gold bars the machine can produce in one day before breaking down
            1 <= G <=1E12
    Return:
        The # of day 1 gold production values that would eventually result in exactly G gold bars
            Day 1 production need to be a positive integer

    Examples:
    - 10
        - 1, 2, 3, 4
        - 10
    - 125
        - 8
        - 23
        - 62
        - 125

    Obs:
    - The answer is at least 1 (just product G on first day)

    Bruteforce:
    - Check all Day 1 values in range [1..G]
    - For each Day 1 value, keep counting up until the total is >= G, at that point check the total and see whether it equals to G (if yes, add 1 to count, otherwise continue)

    TIME: O(G * log(G))
    SPACE: O(1)

    - We're not reusing partial sums (?)

    - sum(K..N) = (K+N) * N / 2
        (N >= K)
        K is a valid starting point <=> there exist N where N >= K s.t. (K+N) * (N-K+1) / 2 = G
    - Binary search? ^^
    - K <= N <= G

    - Bottlenck: Large # of K to try
    - The sums are alternating between odd and even as we add more numbers
    '''
    assert G >= 1

    num_valid = 0   # Counter for valid starting values
    for K in range(1, G+1):
        if is_valid_K(K, G):
            num_valid += 1
        
    return num_valid

def is_valid_K(K, G):
    assert 1 <= K <= G

    i, j = K, G
    # Invariant: sum([K..i)) < G; sum([K..j]) >= G
    while i < j:
        M = (i+j) // 2
        if (K+M) * (M-K+1) // 2 < G:
            i = M + 1
        else:
            j = M
    
    return (K+j) * (j-K+1) // 2 == G


def num_gold_bars_alt(G):
    '''
    Given:
        G: Max # of gold bars the machine can produce in one day before breaking down
            1 <= G <=1E12
    Return:
        The # of day 1 gold production values that would eventually result in exactly G gold bars
            Day 1 production need to be a positive integer

    Examples:
    - 10
        - 1, 2, 3, 4
        - 10
    - 125
        - 8
        - 23
        - 62
    '''
    assert G >= 1

    num_valid = 0  # Count of # of valid Day 1 productions
    i, j = 1, get_right(1, G)

    # Proposition: j <= G => i ends up being = j = G
    while i <= G:
        partial_sum = (i+j) * (j-i+1) // 2
        if partial_sum == G:
            num_valid += 1
            i += 1
        elif partial_sum < G:
            j = get_right(i, G)
        else:
            i = get_left(j, G) 
    
    return num_valid

def get_right(i, G):
    '''Return smallest value `j` s.t. sum([i..j]) >= G'''
    assert 1 <= i <= G

    l, r = i, G
    # Invariant: sum([i..l)) < G; sum([i..r]) >= G
    while l < r:
        M = (l+r) // 2
        if (i+M) * (M-i+1) // 2 < G:
            l = M + 1
        else:
            r = M
    
    return r


def get_left(j, G):
    '''Return smallest value `i` s.t. sum([i..j]) <= G'''
    assert 1 <= j <= G

    l, r = 1, j
    # Invariant: sum([l..j]) > G; sum((r..j]) <= G
    while l < r:
        M = ceil((l+r) / 2)
        if (M+j) * (j-M+1) // 2 > G:
            l = M
        else:
            r = M - 1
    
    return l+1


def num_gold_bars(G):
    '''
    Given:
        G: Max # of gold bars the machine can produce in one day before breaking down
            1 <= G <=1E12
    Return:
        The # of day 1 gold production values that would eventually result in exactly G gold bars
            Day 1 production need to be a positive integer

    Examples:
    - 10
        - 1, 2, 3, 4
        - 10
    - 125
        - 8
        - 23
        - 62
    '''
    assert G >= 1

    eps = 1E-8
    num_valid = 0    
    H = ceil(sqrt(2 * G))
    for k in range(0, H+1):
        i = G/(k+1) - k/2
        if i >= 1 and i%1 <= eps:
            num_valid += 1
    
    return num_valid



INPUT_FILE = './input-hard.txt'
ANS_FILE = './ans-hard.txt'
# SKIPPED = [18, 23, 48]
SKIPPED = []

if __name__ == '__main__':
    with open(INPUT_FILE, 'r') as f:
        with open(ANS_FILE, 'r') as g:
            t = int(f.readline().strip())
            for i in range(1, t+1):
                if i in SKIPPED:
                    f.readline()
                    g.readline()  # Skip this testcase
                    continue 
                else:
                    G = int(f.readline().strip())
                    res = num_gold_bars(G)
                    ans_string = f"Case #{i}: {res}"
                    correct_string = g.readline().strip()
                    print(ans_string)
                    assert ans_string == correct_string, f"Returned string: {ans_string}. Correct string: {correct_string}"
                
            print()
            print('All tests passed!')
    # pass
