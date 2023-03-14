from partition import partition3

def qsort_naive(arr):
    '''
    Return a copy of the sorted array of `arr`
    A criticism of this implementation of quicksort is the creation and destruction of lists

    :params:
    :arr    The input array to be sorted
    '''
    if len(arr) < 2:
        return arr
    
    p = arr[0]
    left = [x for x in arr[1:] if x < p]
    right = [x for x in arr[1:] if x >= p]
    return qsort_naive(left) + [p] + qsort_naive(right)

def qsort_insitu(arr, i, j):
    '''
    Sorts arr[i..j) in-place
    '''
    if j-i < 2:
        return

    l, r = partition3(arr, i, j)  # lis[i..l) < pivot; lis[r..j) > pivot
    qsort_insitu(arr, i, l)
    qsort_insitu(arr, r, j)
    

def qsort_tail(arr, i, j):
    '''
    A further optimisation of `qsort_insitu` that eliminates tail recursion
    '''
    while j-i > 1:
        l, r = partition3(arr, i, j)  # lis[i..l) < pivot; lis[r..j) > pivot
        if l-i < j-r:
            qsort_tail(arr, i, l)
            i = r
        else:
            qsort_tail(arr, r, j)
            j = l



testcases = [
    ([2,4,1,5,0], [0,1,2,4,5]),
    ([], []),
    ([1], [1]),
    ([1,2,3,4,5], [1,2,3,4,5]),
    ([5,4,3,2,1], [1,2,3,4,5])
]

if __name__ == '__main__':
    for i in range(len(testcases)):
        input = testcases[i][0]
        qsort_tail(input, 0, len(testcases[i][0]))
        if input == testcases[i][1]:
            print(f'PASSED: Test #{i+1}')
        else:
            print(f'FAILED: Test #{i+1}. Expected {testcases[i][1]}. Function returned {input}')
