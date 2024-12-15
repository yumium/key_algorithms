# Source: https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933

def cutting_intervals_orig(N, C, intervals):
    '''
    Given:
        N: The # of intervals
            1 <= N <= 1E5
        C: The maximum # of cuts
            1 <= C <= 1E18
        intervals: A list of (L_i, R_i) tuples representing boundaries of an interval
            1 <= L_i < R_i <= 1E13; L_i and R_i are integers
    Return:
        The maximum # of intervals obtained through at most C cuts

    A cut at X cuts through all intervals [L,R] where L < X < R.
    This creates new intervals [L,X] and [X,R]
    X is an integer
    Cutting at the boundary does not create new intervals

    Obs:
    - We cannot create singleton intervals (as that require cuts at the boundary)
    - More cuts is always better than less cuts => use up all C cuts
        - With unlimited cuts, we cut on every integer that is within some interval, this will maximally cut all intervals

    Examples:
    - [1,3], [2,4], [1,4]; maximum 3 cuts

    Bruteforce:
    TIME: O((K choose C) * N * C) = O(K! * N * C)
    SPACE: O(K)
    '''
    count = {}  # integer => # of intervals that surrounds it

    for L, R in intervals:
        for x in range(L+1, R):
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
    
    if C >= len(count):
        return sum(count.keys()) + N
    else:
        return sum(top_k(count.keys(), C)) + N
    

def top_k(arr, k):
    pass

import heapq

def cutting_intervals(N, C, intervals):
    # Min and max value to cut
    min_value = None
    max_value = None

    start = {}
    end = {}
    for L, R in intervals:
        if R-L == 2:
            increment_counter(start, L+1)
            increment_counter(end, L+1)
            if min_value is None or L+1 < min_value:
                min_value = L+1
            if max_value is None or max_value < L+1:
                max_value = L+1
        elif R-L > 2:
            increment_counter(start, L+1)
            increment_counter(end, R-1)
            if min_value is None or L+1 < min_value:
                min_value = L+1
            if max_value is None or max_value < R-1:
                max_value = R-1

    num_active = 0  # Number of active intervals (intervals that surround the current number `x`)
    top_cuts = []  # Top intervals to cut, values represent # of additional intervals if cut there
    for x in range(min_value, max_value+1):
        if x in start:
            num_active += start[x]
        heapq.heappush(top_cuts, num_active)
        if len(top_cuts) > C:
            heapq.heappop(top_cuts)
        if x in end:
            num_active -= end[x]

    return sum(top_cuts) + N


def increment_counter(counter, val):
    if val in counter:
        counter[val] += 1
    else:
        counter[val] = 1

INPUT = './input-hard.txt'
ANS = './ans-hard.txt'

if __name__ == '__main__':
    with open(INPUT, 'r') as f:
        with open(ANS, 'r') as g:
            t = int(f.readline().strip())
            for i in range(1, t+1):
                [N, C] = [int(x) for x in f.readline().strip().split(' ')]
                intervals = []
                for cnt in range(N):
                    intervals.append(tuple([int(x) for x in f.readline().strip().split(' ')]))
                
                ans = cutting_intervals(N, C, intervals)
                ans_string = f"Case #{i}: {ans}"
                correct_string = g.readline().strip()
                print(ans_string)
                assert ans_string == correct_string, ans_string + ", " + correct_string

    print("All tests passed!")

