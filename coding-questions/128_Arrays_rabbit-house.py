# Google Kickstart: 2021 - Round A

def make_safe_first(R, C, grid):
    '''
    Given:
        R: rows of grid
        C: cols of grid
        grid: 2D grid of non-negative integers for height
        
            1 <= R, C <= 300
            0 <= grid_ij <= 2E6
    
    Return:
        The minimum box additions to make the grid safe
            A safe grid is one that adjacent cells have height difference no more than 1
    Obs:
    - Can always make grid safe by adding boxes so that every cell has equal height
    - For each cell, adjacent cells that are too short need to be brought to its height - 1. This is necessary
    - The grid is qualified if all cells are good with its neighbours
    - We can prove easily by construction that if we go from the heighest cell, raising its neighbours to cell_height-1, and iterate down to the next heightest cells etc. we will
        - Get a safe grid
        - This safe grid requires the least changes, as all changes are necessary

    TIME: O(R^2 * C^2)
    SPACE: O(R*C)
    '''
    last_height = 2E6 + 1
    # print(last_height)
    
    res = 0  # number of boxes added
    
    while True:
        cur_height = -1
        cells = []  # A list of (i,j) to sort out its neighbours
        # Search for heighest cell that is below `last_height`
        for i in range(R):
            for j in range(C):
                cell_height = grid[i][j]
                if cell_height < last_height:
                    # print('here')
                    if cell_height == cur_height:
                        cells.append((i,j))
                    elif cell_height > cur_height:
                        cur_height = cell_height
                        cells = [(i,j)]

        if cur_height == -1:
            break
        
        # Sort out selected cells
        for i, j in cells:
            if i-1 >= 0 and grid[i-1][j] < cur_height-1:
                delta = cur_height - 1 - grid[i-1][j]
                res += delta
                grid[i-1][j] += delta
            if i+1 < R and grid[i+1][j] < cur_height-1:
                delta = cur_height - 1 - grid[i+1][j]
                res += delta
                grid[i+1][j] += delta
            if j-1 >= 0 and grid[i][j-1] < cur_height-1:
                delta = cur_height - 1 - grid[i][j-1]
                res += delta
                grid[i][j-1] += delta
            if j+1 < C and grid[i][j+1] < cur_height-1:
                delta = cur_height - 1 - grid[i][j+1]
                res += delta
                grid[i][j+1] += delta
        
        last_height = cur_height

    return res
    
import heapq
def make_safe_heap(R, C, grid):
    '''
    To make the algorithm run faster, we can store a mapping from height to cells via a hash table, and keep track of all the heights with a max heap
    Note, we only need to add new heights from changes to the heap. We don't need to remove heights from heap (just hash table) as that is slow. When we encounter a height from the max heap that is not in the hash table, we can just ignore it

    TIME: O(R*C log(R*C))
    SPACE: O(R*C)
    '''
    cells = {}  # height => list of indices with that height
    for i in range(R):
        for j in range(C):
            cell_height = grid[i][j]
            if cell_height not in cells:
                cells[cell_height] = [(i,j)]
            else:
                cells[cell_height].append((i,j))

    heights = [-k for k in cells.keys()]  # Heights stored as negative
    heapq.heapify(heights)

    res = 0  # number of boxes added
    
    while True:
        # Search for heighest cell that is below `last_height`
        while len(heights) > 0 and -heights[0] not in cells:
            heapq.heappop(heights)

        if len(heights) == 0:
            break
        
        cur_height = -heapq.heappop(heights)
        selected = cells[cur_height] # A list of (i,j) to sort out its neighbours
        del cells[cur_height]
        # Sort out selected cells
        for i, j in selected:
            if i-1 >= 0 and grid[i-1][j] < cur_height-1:
                delta = cur_height - 1 - grid[i-1][j]
                res += delta
                increase_height(i-1, j, grid[i-1][j], delta, cells, heights)
                grid[i-1][j] += delta
            if i+1 < R and grid[i+1][j] < cur_height-1:
                delta = cur_height - 1 - grid[i+1][j]
                res += delta
                increase_height(i+1, j, grid[i+1][j], delta, cells, heights)
                grid[i+1][j] += delta
            if j-1 >= 0 and grid[i][j-1] < cur_height-1:
                delta = cur_height - 1 - grid[i][j-1]
                res += delta
                increase_height(i, j-1, grid[i][j-1], delta, cells, heights)
                grid[i][j-1] += delta
            if j+1 < C and grid[i][j+1] < cur_height-1:
                delta = cur_height - 1 - grid[i][j+1]
                res += delta
                increase_height(i, j+1, grid[i][j+1], delta, cells, heights)
                grid[i][j+1] += delta
        
    return res
    
def increase_height(i, j, orig_height, delta, cells, heights):
    if len(cells[orig_height]) == 1:
        del cells[orig_height]
    else:
        cells[orig_height].remove((i,j))
    
    if orig_height + delta in cells:
        cells[orig_height + delta].append((i,j))
    else:
        cells[orig_height + delta] = [(i,j)]
        heapq.heappush(heights, -(orig_height+delta))


def make_safe(R, C, grid):
    '''
    Let G be the height of the tallest cell in the grid.
    Then the final grid will have heights no less than G-R-C+2
    This means we can use an array of length O(R+C) to store the cells!

    TIME: O(R*C)
    SPACE: O(R*C)
    '''
    G = max([max(row) for row in grid])
    cells = [None]*(R+C-1)  # cell[i] = cells with height i+G-R-C+2

    # populate cells
    for i in range(R):
        for j in range(C):
            if grid[i][j] >= G-R-C+2:
                idx = grid[i][j]-G+R+C-2
                if cells[idx] is None:
                    cells[idx] = [(i,j)]
                else:
                    cells[idx].append((i,j))

    res = 0  # number of boxes added

    for h in range(len(cells)-1, -1, -1):
        if cells[h] is None:
            continue

        for i, j in cells[h]:
            cur_height = grid[i][j]

            if i-1 >= 0 and grid[i-1][j] < cur_height-1:
                res += update_cell(R, C, grid, G, cells, i-1, j, cur_height)

            if i+1 < R and grid[i+1][j] < cur_height-1:
                res += update_cell(R, C, grid, G, cells, i+1, j, cur_height)

            if j-1 >= 0 and grid[i][j-1] < cur_height-1:
                res += update_cell(R, C, grid, G, cells, i, j-1, cur_height)

            if j+1 < C and grid[i][j+1] < cur_height-1:
                res += update_cell(R, C, grid, G, cells, i, j+1, cur_height)

    return res


def update_cell(R, C, grid, G, cells, i, j, cur_height):
    '''
    Updates `cells` and return delta
    '''
    delta = cur_height - 1 - grid[i][j]

    # Remove from old cell, if needed
    if grid[i][j] >= G-R-C+2:
        cells[grid[i][j]-G+R+C-2].remove((i,j))

    # Update grid
    grid[i][j] = cur_height - 1

    if cells[cur_height-1-G+R+C-2] is None:
        cells[cur_height-1-G+R+C-2] = [(i,j)]
    else:
        cells[cur_height-1-G+R+C-2].append((i,j))

    return delta


# INPUT = './coding-questions/input.txt'
INPUT = 'in.txt'
# ANS = './coding-questions/ans.txt'
ANS = 'ans.txt'


def main():
    with open(INPUT, 'r') as f:
        with open(ANS, 'r') as g:
            t = int(f.readline())
            for i in range(1, t+1):
                [R,C] = [int(s) for s in f.readline().strip().split(' ')]
                grid = []
                for j in range(R):
                    grid.append([int(s) for s in f.readline().split(' ')])
                out = "Case #{0}: {1}".format(i, make_safe(R, C, grid))
                correct = g.readline().strip()
                print(out)
                assert out == correct, f'Algorithm output {out}, correct output {correct}'

if __name__ == '__main__':
    main()
