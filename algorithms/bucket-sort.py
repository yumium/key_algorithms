# $$
def bucketsort(arr, n):
    '''
    Returns the sorted the array of *arr* given that the elements in *arr* are integers in range [0..n)
    '''
    count = [0] * n
    res = [None] * len(arr)

    for num in arr:
        count[num] += 1
    
    for i in range(1, n):
        count[i] += count[i-1]

    for i in range(len(arr)-1, -1, -1):
        res[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return res






