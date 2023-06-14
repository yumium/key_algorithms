def partition(lis, l, r):
    '''
    Given a list, and pointers indicating the segment ( lis[l..r) ), the function will give a permutation of lis where:
        lis[l..i) < val; lis[i..r) >= val; specifically lis[i] == val
            where: val = lis0[l]
    Then return i

    Pre: lis non-empty
    '''

    val = lis[l]
    i, j = l+1, r
    # Invariant: lis[l+1..i) < val; lis[j..r) >= val; l+1 <= i <= j <= r
    # Variant: j-i
    while i < j:
        if lis[i] < val:
            i += 1
        else:
            j -= 1
            lis[i], lis[j] = lis[j], lis[i]

    lis[i-1], lis[l] = lis[l], lis[i-1]
    return i-1

def partition3(lis, l, r):
    '''
    Given a list, and pointers indicating the segment ( lis[l..r) ), the function will give a permutation of lis where:
        lis[l..i) < val; lis[i..j) = val; lis[j..r) > val
            where: val = lis0[l]
    Then return (i,j)

    Pre: lis non-empty
    '''

    val = lis[l]
    i, j, k = l+1, l+1, r
    # Invariant: lis[l+1..i) < val; lis[i..j) = val; lis[k..r) > val; l+1 <= i <= j <= k <= r
    # Variant: k-j
    while j < k:
        if lis[j] < val:
            lis[i], lis[j] = lis[j], lis[i]
            i += 1; j += 1
        elif lis[j] == val:
            j += 1
        else:
            k -= 1
            lis[j], lis[k] = lis[k], lis[j]

    lis[i-1], lis[l] = lis[l], lis[i-1]
    return (i-1, j)
