class Solution:
    def spiralOrder(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = [matrix[0][0]]
        matrix[0][0] = None

        cur_dir = 'E'
        i, j = 0, 0 # Pointers tracking the current cell

        while len(res) < ROWS * COLS:
            if cur_dir == 'E':
                while j+1 < COLS and matrix[i][j+1] is not None:
                    print('Going East')
                    res.append(matrix[i][j+1])
                    matrix[i][j+1] = None
                    j += 1
                cur_dir = 'S'

            if cur_dir == 'S':
                while i+1 < ROWS and matrix[i+1][j] is not None:
                    print('Going South')
                    res.append(matrix[i+1][j])
                    matrix[i+1][j] = None
                    i += 1
                cur_dir = 'W'
                
            if cur_dir == 'W':
                while j-1 >= 0 and matrix[i][j-1] is not None:
                    print('Going West')
                    res.append(matrix[i][j-1])
                    matrix[i][j-1] = None
                    j -= 1
                cur_dir = 'N'

            if cur_dir == 'N':
                while i-1 >= 0 and matrix[i-1][j] is not None:
                    print('Going North')
                    res.append(matrix[i-1][j])
                    matrix[i-1][j] = None
                    i -= 1
                cur_dir = 'E'

        return res
    

    def spiralOrder2(self, matrix):
        t, d, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = [matrix[0][0]]
        i, j = 0, 0

        while t <= d and l <= r:
            while j+1 <= r:
                j += 1; res.append(matrix[i][j])
            t += 1
            if t > d: break

            while i+1 <= d:
                i += 1; res.append(matrix[i][j])
            r -= 1
            if l > r: break

            while j-1 >= l:
                j -= 1; res.append(matrix[i][j])
            d -= 1
            if t > d: break

            while i-1 >= t:
                i -= 1; res.append(matrix[i][j])
            l += 1
            if l > r: break

        return res


    
myMatrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

myMatrix2 = [[1]]

myMatrix3 = [[1,2,3,4,5]]

myMatrix4 = [[1],[2],[3],[4],[5]]

sol = Solution()