# Source: https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b44ef

def banana_bunches_orig(N, B, K):
    '''
    Given:
        N: The # of banana trees
            1 <= N <= 5000
        B: A list of banana bunches on each tree
            0 <= B_i <= K
        K: Capacity of the basket
            1 <= 1E6
    Return:
        The minimum # of trees to farm to get exactly K bananas
        We have constraint that we can farm at most 2 contiguous sections
        Return -1 if impossible

    Example:
    - K = 8, B = [1, 2, 3, 1, 2, 3]
        3 trees
    - K = 10, B = [6, 7, 5, 2]
        -1
    - K = 8, B = [3, 1, 2, 1, 3, 1]
        4 ([3,1,2,1])
    - K = 6, B = [3, 2, 1, 0]
        3
    
    TIME: O(K * N * N)
    SPACE: O(1)

    Ideas:
    - Merge the 2 sections
    - Given an array, finding all subarrays with target sum is linear
    '''
    res = -1  # Smallest # of trees to farm to get `K` # of bananas

    # Trying 1 contiguous section
    ans = smallest_subarray(B, 0, len(B), K)
    if ans is not None:
        l0, r0 = ans
        res = r0 - l0
    
    # Trying 2 contiguous sections
    for x in range(1, K//2 + 1):
        for l, r in candidate_subarrays(B, x):
            # if x == 355:
            #     print(l,r)
            len_other = None  # Smallest length of second section

            for i, j in [(0, l), (r, len(B))]:
                other = smallest_subarray(B, i, j, K-x)
                # if x == 355:
                #     print(B, i, j, K-x)
                if other is not None:
                    l0, r0 = other
                    if len_other is None or len_other > r0-l0:
                        len_other = r0 - l0

            if len_other is not None and (res == -1 or res > (r-l) + len_other):
                res = (r-l) + len_other
    
    return res


def smallest_subarray(arr, i, j, target):
    '''
        Return (l,r) where sum(arr[l..r)) = target and it is the smallest subarray in arr[i..j) with this property
        Return `None` if impossible
    '''
    assert j >= i
    assert target > 0

    if j == i:
        return None
    
    l0 = r0 = None  # Index boundary of smallest subarray in arr[i..j) with sum equal to `target`
    total = 0
    l = r = i
    # Invariant: total = arr[l..r) && l <= r && (r < j or (r = j and arr[l..r) < target))
    while r < j or total >= target:
        # print(l, r)
        # print(total)
        if arr[l] == 0:
            l += 1
            if r < l:
                if r == j:
                    break
                else:
                    r += 1
        
        elif total < target:
            total += arr[r]
            r += 1

        elif total == target:
            if l0 is None or r0-l0 > r-l:
                l0 = l; r0 = r
            if r == j:
                break
            total += arr[r]
            r += 1

        else:
            total -= arr[l]
            l += 1

    if l0 is None:
        return None
    else:
        return (l0, r0)
    

def candidate_subarrays(arr, target):
    '''
        Return a list of (l,r) where sum(arr[l..r)) = target
        For each `l`, return the smalleset `r` with that property only
        Skip all `l` where arr[l] = 0
    '''
    assert len(arr) > 0
    target > 0

    candidates = []
    total = 0
    l = r = 0
    # Invariant: total = arr[l..r) && l <= r && (r < j or (r = j and arr[l..r) < target))
    while r < len(arr) or total >= target:
        if arr[l] == 0:
            l += 1
            if r < l:
                if r == len(arr):
                    break
                else:
                    r += 1
        
        elif total < target:
            total += arr[r]
            r += 1

        elif total == target:
            candidates.append((l,r))
            total -= arr[l]
            l += 1

        else:
            total -= arr[l]
            l += 1

    return candidates

# The weakness of the original method is the dependency of runtime on K
# There is plenty of room for optimisation here, as for many values of x, x <= K, the value can never be achieved with a subarray of B
# In other words, it's quicker to check through possible sums of subarrays than all possible value of x, x <= K
# The algorithm below does exactly that

def banana_bunches(N, B, K):
    inf = len(B) + 1  # Our pseudo infinity value
    best = [inf] * (K+1)

    ans = inf

    # single = smallest_subarray(B, 0, len(B), K)
    # if single is not None:
    #     l, r = single
    #     ans = r-l

    i = N
    while i > 0:
        currSum = 0
        for j in range(i-1, -1, -1):
            # currSum = sum(arr[j..i))
            currSum += B[j]
            if currSum == K:
                ans = min(ans, i-j)
            elif currSum < K:
                # best[k] = min length of subarray starting after index i which has sum equal to K - currSum
                ans = min(ans, i-j+best[K-currSum])

        # update `best` array    
        currPostSum = 0
        i -= 1
        for x in range(i, len(B)):
            # curPostSum = sum(arr[i..x])
            currPostSum += B[x]
            if currPostSum <= K:
                best[currPostSum] = min(best[currPostSum], x-i+1)

    return -1 if ans == inf else ans

INPUT = './input-hard.txt'
ANS = './ans-hard.txt'

if __name__ == '__main__':
    with open(INPUT, 'r') as f:
        with open(ANS, 'r') as g:
            t = int(f.readline().strip())
            for i in range(1, t+1):
                N, K = [int(x) for x in f.readline().split(' ')]
                B = [int(x) for x in f.readline().split(' ')]
                ans = banana_bunches(N, B, K)
                ans_string = f"Case #{i}: {ans}"
                correct_string = g.readline().strip()
                if ans_string == correct_string:
                    print(ans_string)
                else:
                    print(f"INCORRECT: {ans_string}, {correct_string}, i = {i}, N = {N}, K = {K}")



    # print(smallest_subarray([116,239,1957,782,592,247,68], 2, 7, 1689))
    # print(banana_bunches(7, [116,239,1957,782,592,247,68], 2044))
    # print(sum([116,239,1957,782,592,247,68]))

'''
7 2044
116 239 1957 782 592 247 68
'''



# print(banana_bunches(6, [1,2,3,1,2,3], 8))
# print(banana_bunches(4, [6,7,5,2], 10))
# print(banana_bunches(6, [3,1,2,1,3,1], 8))
# print(banana_bunches(4, [3,2,1,0], 6))
