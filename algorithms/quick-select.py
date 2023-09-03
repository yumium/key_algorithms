import random
from partition import partition3

def quickselect3(arr, i, j, k):
    '''
    Same as quickselect but this function is fine with non-distinct elements in `arr`
    Returns: The value of the k-th smallest element in arr[i..j); will also partition `arr` s.t. k smallest elements in arr[i..j) are in arr[i..i+k)
    '''
    assert 0 <= i < j <= len(arr)
    assert 1 <= k <= j-i

    # Randomise the pivot
    idx = random.randrange(i,j)
    arr[i], arr[idx] = arr[idx], arr[i]

    p, q = partition3(arr, i, j)
    # arr[i..p) < pivot; arr[p..q) = pivot; arr[q..j) > pivot
    if p-i < k <= q-i:
        return arr[p]
    elif k <= p-i:
        return quickselect3(arr, i, p, k)
    else:
        return quickselect3(arr, q, j, k-(q-i))
