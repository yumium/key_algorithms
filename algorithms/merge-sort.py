def mergesort(arr, i, j):
    '''
    Sorts arr[i..j)
    Pre: 0 <= i <= j <= len(arr)
    '''
    if j - i >= 2:
        i, j, k = i, (i+j)//2, j
        mergesort(arr, i, j)
        mergesort(arr, j, k)
        merge(arr, i, j, k)

    
def merge(arr, i, j, k):
    '''
    Sorts arr[i..k) given arr[i..j) and arr[j..k) are sorted
    Pre: 0 <= i < j < k <= len(arr)
    '''
    a = arr[i:j]
    b = arr[j:k]

    ai, bi, aEnd, bEnd = 0, 0, j-i, k-j
    # Invariant: arr[i0..i) is sorted perm. of arr[i0..k)
    while ai < aEnd:    # Because ai < aEnd also implies i < k 
        if bi == bEnd or a[ai] <= b[bi]:
            arr[i] = a[ai]
            ai += 1
        else:
            arr[i] = b[bi]
            bi += 1
        i += 1


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
        mergesort(input, 0, len(input))
        if input == testcases[i][1]:
            print(f'PASSED: Test #{i+1}')
        else:
            print(f'FAILED: Test #{i+1}. Expected {testcases[i][1]}. Function returned {input}')
