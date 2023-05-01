def find(val, lis):
    '''
    Returns the index of the FIRST occurence of the value, returns -1 if not found (js convention). Assumption, lis is sorted. Elements in lis does not need to be distinct.
        val: the value
        lis: the list, sorted
    '''

    # Invariant: lis[0..i) < val; lis[j..N) >= val; 0 <= i <= j <= N
    i, j = 0, len(val)
    while i < j:
        m = (i+j) // 2
        if lis[m] < val:
            i = m+1
        else:
            j = m

    return i if i < len(lis) and lis[i] == val else -1
