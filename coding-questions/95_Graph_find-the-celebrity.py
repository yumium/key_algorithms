# Source: https://www.geeksforgeeks.org/the-celebrity-problem/

def know(a, b):
    '''
    Returns if a knows b (a -> b)
    '''
    return True

def findCelebrity(n):
    '''
    Given:
        n: The # of people in the party (person are integers between 1 and n inclusive)
    Return:
        integer of celebrity, or -1 if none exist
        A celebrity is someone that everyone else knows but don't know anyone themselves
        You only have access to the `know` function, find a solution that queries this functions the least
    
    Observations:
    - There can be at most 1 celebrity
    - When we check a -> b. If it's true, then a can't be celebrity. If it's false, then b can't be celebrity. This means each check eliminates 1 person, giving an O(N) algorithm
    '''
    assert n >= 1

    candidate = 1
    # Invariant: candidate is the only person that may be a celebrity in persons [1..p)
    for p in range(2, n+1):
        if know(p, candidate):
            continue
        else:
            candidate = p
    
    for p in range(1, n+1):
        if p != candidate and (not know(p, candidate) or know(candidate,p)):
            return -1
    return candidate
