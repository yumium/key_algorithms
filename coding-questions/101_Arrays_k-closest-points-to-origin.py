# Source: https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Given:
            points: list of binary lists representing [x,y] coords
            k: k cloest points
                1 <= k <= len(points) <= 1E4
                -1E4 < x, y < 1E4
        Return:
            A list of k closest points to origin [0,0]
                List doesn't need to be in any order, guaranteed to be unique
        '''
        # comparator = lambda a, b: a[0]**2 + a[1]**2 <= b[0]**2 + b[1]**2
        key = lambda a: a[0]**2 + a[1]**2

        self.selection(points, 0, len(points), k, key)
        return points[:k]
        
    def selection(self, arr, i, j, k, key):
        # Partition `arr` s.t. arr[i..i+k) are the smallest k elements in arr[i..j)
        a, b = self.partition(arr, i, j, key)

        if a <= i+k-1 < b:
            return
        elif i+k-1 < a:
            self.selection(arr, i, a, k, key)
        else:
            self.selection(arr, b, j, k-(b-i), key)

    def partition(self, arr, i, j, key):
        # Return a, b s.t. arr[i..a) < pivot; arr[a..b) = pivot; arr[b..j) > pivot 
        # Pivot is arr0[i]

        val = key(arr[i])
        a, b, c = i+1, i+1, j
        # Invariant: arr[i+1..a) < val; arr[a..b) = val; arr[c..j) > val
        while c > b:
            if key(arr[b]) < val:
                arr[a], arr[b] = arr[b], arr[a]
                a += 1; b += 1
            elif key(arr[b]) == val:
                b += 1
            else:
                c -= 1
                arr[b], arr[c] = arr[c], arr[b]
        
        arr[i], arr[a-1] = arr[a-1], arr[i]
        return (a-1, b)