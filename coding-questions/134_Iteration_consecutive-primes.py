# Source: Google Kickstart 2021 Round B
from math import sqrt, ceil

def consecutive_primes(z):
    '''
    Given:
        z: An integer
            6 <= z <= 1E18
    Return:
        Integer x where x is the largest number satisfying
            -> x <= z
            -> There are consecutive primes x1 and x2 s.t. x = x1 * x2

    Examples:
    - z = 2021; x = 2021 (43 * 47)
    - z = 2020; x = 1763 (41 * 43)

    Obs:
    - p1, p2, p3 ... (where p1 = 2; p2 = 3; p3 = 5 ...)
    - Let R_i = p_i * p_(i+1)
    - Then, x is the value of R_j where j is the largest s.t. R_j <= z

    - This will always return a valid answer, as 6 <= z

    - Can we use binary search approach?
    - x1 <= sqrt(z)

    - Generating all primes from the ground up can be time consuming
        - Think if z is very large, there is no need to start from 2 and 3
    - It may be more natural to go from a pair of consecutive primes a little bigger than z, and search downwards

    - We can start with x2 as first prime >= ceil(sqrt(z)), this guarantees x1 * x2 cannot be lower than x. We can then go down from there if it's larger
    
    TIME: O(Z^2)
    SPACE: O(1)
    '''
    ps = primes_down(next(primes(ceil(sqrt(z)))))  # You should be able to find a prime when going up to `z`
    x2 = next(ps)
    x1 = next(ps)
    while x1 * x2 > z:  # while loop body executes at most once => only 3 primes are searched from initial x2
        x2 = x1
        x1 = next(ps)

    return x1 * x2

    # --- OLD SOLUTION --- #

    # ps = primes(2*z)  # Giving a higher range would not require extra computation
    
    # r_prev = None
    # x1 = ps.next
    # x2 = ps.next
    # r = x1 * x2
    # # Invariant: x1 and x2 are consecutive primes; r = x1 * x2; r_prev is the previous value of `r` or None at beginning
    # while r <= z:
    #     r_prev = r
    #     x1 = x2
    #     x2 = ps.next
    #     r = x1 * x2
    
    # return r_prev


def primes_down(start):
    '''
    Returns an iterator for all primes in range [2..start] from highest to lowest
    '''
    assert start >= 2

    for x in range(start, 4, -1):
        if x%2 == 0 or x%3 == 0:
            continue

        exit = False
        for divisor in range(4, ceil(sqrt(x))+1):
            if x%divisor == 0:
                exit = True
                break
        if exit:
            continue

        yield x

    yield 3
    yield 2


def primes(start):
    '''
    Returns an iterator for all primes from `start`
    '''
    assert start >= 2
    if 2 >= start:
        yield 2
    if 3 >= start:
        yield 3
    
    x = max(5, start)
    x -= 1 # Cancel out first iteration of increment
    while True:
        x += 1
        if x%2 == 0 or x%3 == 0:
            continue

        exit = False
        for divisor in range(4, ceil(sqrt(x))+1):
            if x%divisor == 0:
                exit = True
                break
        if exit:
            continue
        
        yield x

INPUT = './coding-questions/input-medium.txt'
ANS = './coding-questions/ans-medium.txt'

def main():
    with open(INPUT, 'r') as f:
        with open(ANS, 'r') as g:
            t = int(f.readline())
            for i in range(1, t+1):
                z = int(f.readline())
                ans = consecutive_primes(z)
                output_string = f"Case #{i}: {ans}"
                correct_string = g.readline().strip()
                print(output_string)
                assert output_string == correct_string, output_string + ', ' + correct_string

if __name__ == '__main__':
    main()
