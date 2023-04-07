import random
from partition import partition3

def quickselect3(arr, i, j, k):
    '''
    Same as quickselect but this function is fine with non-distinct elements in `arr`
    Pre: 1 <= k <= j-i; 0 <= i < j <= len(arr)
    Returns: The value of the k-th smallest element in arr[i..j); will also partition `arr` s.t. k smallest elements in arr[i..j) are in arr[i..i+k)
    '''
    # Randomise the pivot
    idx = random.randrange(i,j)
    arr[i], arr[idx] = arr[idx], arr[i]

    p, q = partition3(arr, i, j)

    if p <= i+k-1 < q:
        return arr[p]
    elif p > i+k-1:
        return quickselect3(arr, i, p, k)
    else:
        return quickselect3(arr, q, j, k-(q-i))