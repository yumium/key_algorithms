# Source: https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd

EMPTY = '.'
BLACK = '#'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# def palindromic_crossword_orig(N, M, grid):
#     '''
#     Given:
#         N: # of rows
#         M: # of cols
#             1 <= N,M <= 1000
#         grid: The matrix of partially-filled crossword puzzle
#             A-Z are filled cells
#             . are empty cells
#             # are black cells
#     Return:
#         The grid raplced by capital letter where possible
    
#     Example:
#     A...#.
#     A...#.
#     B##...
#     B.###.
#     A...#.
    
#     becomes

#     A..A#.
#     B##A.A
#     BB###A
#     ABBA#.

#     ---

#     A.
#     .#
    
#     becomes

#     AA
#     A#


#     Obs:
#     - If the grid is empty, we cannot infer anything
#     - Any addition of characters can trigger more addition of characters
#     - There can be no contradictions (e.g. A.B#)
    
#     Continuously:
#     1. Iterate through all the crosswords
#     2. Remember new characters that can be filled
#     3. Apply all changes
#     4. Repeat until no changes in an iteration

#     TIME: O((N*M)^2)
#     SPACE: O(N*M)
#     '''
#     changes = set()  # Set tracking the changes in current iteration
#     changed = True  # Boolean indicating whether last iteration had any changes, starts with true so we always do 1 iteration
#     while changed:
#         # Rows
#         for i in range(N):
#             i_start = j_start = None  # starting index of the latest word (horizontal)
#             for j in range(M):
#                 if grid[N][M] != BLACK:
#                     if i_start is None:
#                         i_start = i
#                         j_start = j
#                 else:
#                     if i_start is not None:
#                         changes |= fill_characters(grid, i_start, j_start, j-j_start, 'ROW')
#                         i_start = j_start = None
            
#             if i_start is not None:
#                 changes |= fill_characters(grid, i_start, j_start, j-j_start, 'ROW')

#         # Cols
#         for j in range(M):
#             i_start = j_start = None  # starting index of the latest word (horizontal)
#             for i in range(N):
#                 if grid[N][M] != BLACK:
#                     if i_start is None:
#                         i_start = i
#                         j_start = j
#                 else:
#                     if i_start is not None:
#                         changes |= fill_characters(grid, i_start, j_start, i-i_start, 'COL')
#                         i_start = j_start = None
            
#             if i_start is not None:
#                 chaneges |= fill_characters(grid, i_start, j_start, i-i_start, 'COL')

#         if len(changes) == 0:
#             changed = False
#         else:
#             for ((i,j), char) in changes:
#                 grid[i][j] = char

#     return grid    


# def fill_characters(grid, i, j, length, mode):
#     '''
#     :param:
#     :length int
#         Length of the crossword
#     :mode   string
#         The direction of the crossword ('ROW' or 'COL')
    
#     Return:
#         A set of tuples ((i',j'), character) to be added
#     '''
#     changes = set()  # Changes of characters that can be inferred

#     if mode == 'ROW':
#         for col in range(0, (length-1)//2 + 1):
#             if grid[i][j+col] != EMPTY and grid[i][j+length-1-col] == EMPTY:
#                 changes.add(((i,j+length-1-col), grid[i][j+col]))
#             elif grid[i][j+col] == EMPTY and grid[i][j+length-1-col] != EMPTY:
#                 changes.add(((i,j+col), grid[i][j+length-1-col]))
    
#     else:
#         for row in range(0, (length-1)//2 + 1):
#             if grid[i+row][j] != EMPTY and grid[i+length-1-row][j] == EMPTY:
#                 changes.add(((i+row,j), grid[i+length-1-row][j]))
#             elif grid[i+row][j] == EMPTY and grid[i+length-1-row][j] != EMPTY:
#                 changes.add(((i+length-1-row,j), grid[i+row][j]))

#     return changes


def palindromic_crossword(N, M, grid):
    '''
    Given:
        N: # of rows
        M: # of cols
            1 <= N,M <= 1000
        grid: The matrix of partially-filled crossword puzzle
            A-Z are filled cells
            . are empty cells
            # are black cells
    Return:
        The grid raplced by capital letter where possible
    
    Example:
    A...#.
    A...#.
    B##...
    B.###.
    A...#.
    
    becomes

    A..A#.
    B##A.A
    BB###A
    ABBA#.

    ---

    A.
    .#
    
    becomes

    AA
    A#


    Obs:
    - If the grid is empty, we cannot infer anything
    - Any addition of characters can trigger more addition of characters
    - There can be no contradictions (e.g. A.B#)
    - Every character can only affect at most 2 crosswords (row & col)
        - That is, it can only affect at most 2 extra squares
        - Once we have check those squares, we don't need to check that character again
    - ^^ The naive algorithm is slow because we keep checking the same squares each iteration
    - We just need to check through all squares that will eventually be inferred once
    - If we imagine an edge between each pair, then the resulting characters will form a connected component
    - So we just need to do a DFS but the edges are between pairs in crosswords, filling in the words as we go. This will guarantee to visit all squares in the end as it is connected

    TIME: O(N*M)
    SPACE: O(N*M)
    '''
    neighbours = build_palindrome_graph(grid, N, M)  # (i,j) => [(i',j')] pair in palindrome
    # print(neighbours)

    seen = set()
    for i in range(N):
        for j in range(M):
            if grid[i][j] in ALPHABET and (i,j) not in seen:
                visit(grid, i, j, seen, neighbours)

    return grid


def visit(grid, i, j, seen, neighbours):
    seen.add((i,j))
    for i_other, j_other in neighbours[(i,j)]:
        if (i_other, j_other) not in seen:
            if grid[i_other][j_other] == EMPTY:
                # print('here')
                grid[i_other][j_other] = grid[i][j]
            visit(grid, i_other, j_other, seen, neighbours)


def build_palindrome_graph(grid, N, M):
    neighbours = {}  # (i,j) => [(i',j')] pair in palindrome
    
    # Rows
    for i in range(N):
        i_start = j_start = None  # starting index of the latest word (horizontal)
        for j in range(M):
            if grid[i][j] != BLACK:
                if i_start is None:
                    i_start = i
                    j_start = j
            else:
                if i_start is not None:
                    neighbours = merge_dict(neighbours, get_pair_edges(i_start, j_start, j-j_start, 'ROW'))
                    i_start = j_start = None
        
        if i_start is not None:
            neighbours = merge_dict(neighbours, get_pair_edges(i_start, j_start, M-j_start, 'ROW'))


    # Cols
    for j in range(M):
        i_start = j_start = None  # starting index of the latest word (vertical)
        for i in range(N):
            if grid[i][j] != BLACK:
                if i_start is None:
                    i_start = i
                    j_start = j
            else:
                if i_start is not None:
                    neighbours = merge_dict(neighbours, get_pair_edges(i_start, j_start, i-i_start, 'COL'))
                    i_start = j_start = None
        
        if i_start is not None:
            neighbours = merge_dict(neighbours, get_pair_edges(i_start, j_start, N-i_start, 'COL'))

    return neighbours

def merge_dict(old_dict, new_dict):
    for k, v in new_dict.items():
        if k not in old_dict:
            old_dict[k] = [v]
        else:
            old_dict[k].append(v)

    return old_dict


def get_pair_edges(i, j, length, mode):
    '''
    :param:
    :length int
        Length of the crossword
    :mode   string
        The direction of the crossword ('ROW' or 'COL')
    
    Return:
        A dictionary for edges in this crossword
    '''
    edges = {}
    # print(i, j, length, mode)

    if mode == 'ROW':
        for col in range(0, (length-1)//2 + 1):
            edges[(i,j+length-1-col)] = (i,j+col)
            edges[(i,j+col)] = (i,j+length-1-col)

    else:
        for row in range(0, (length-1)//2 + 1):
            edges[(i+row,j)] = (i+length-1-row,j)
            edges[(i+length-1-row,j)] = (i+row,j)
            
    # print(edges)
    return edges



def fill_characters(grid, i, j, length, mode):
    '''
    :param:
    :length int
        Length of the crossword
    :mode   string
        The direction of the crossword ('ROW' or 'COL')
    
    Return:
        A set of tuples ((i',j'), character) to be added
    '''
    changes = set()  # Changes of characters that can be inferred

    if mode == 'ROW':
        for col in range(0, (length-1)//2 + 1):
            if grid[i][j+col] != EMPTY and grid[i][j+length-1-col] == EMPTY:
                changes.add(((i,j+length-1-col), grid[i][j+col]))
            elif grid[i][j+col] == EMPTY and grid[i][j+length-1-col] != EMPTY:
                changes.add(((i,j+col), grid[i][j+length-1-col]))
    
    else:
        for row in range(0, (length-1)//2 + 1):
            if grid[i+row][j] != EMPTY and grid[i+length-1-row][j] == EMPTY:
                changes.add(((i+row,j), grid[i+length-1-row][j]))
            elif grid[i+row][j] == EMPTY and grid[i+length-1-row][j] != EMPTY:
                changes.add(((i+length-1-row,j), grid[i+row][j]))

    return changes

def count(N, M, grid, values):
    count = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] in values:
                count += 1
    
    return count

def print_grid(N, M, grid):
    out = ''
    for i in range(N):
        row = ''
        for j in range(M):
            row += grid[i][j]
        row += '\n'
        out += row

    return out[:-1] 


INPUT = './input-hard.txt'
ANS = './ans-hard.txt'

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)

    with open(INPUT, 'r') as f:
        with open(ANS, 'r') as g:
            t = int(f.readline().strip())
            for i in range(1, t+1):
                N, M = [int(x) for x in f.readline().strip().split(' ')]
                grid = []
                for _ in range(N):
                    row = list(f.readline().strip())
                    assert len(row) == M
                    grid.append(row)
                assert len(grid) == N

                num_filled_old = count(N, M, grid, ALPHABET) 
                ans = palindromic_crossword(N, M, grid)
                num_filled_new = count(N, M, ans, ALPHABET)

                # print(num_filled_new - num_filled_old)
                # print(print_grid(N, M, ans))

                correct_diff = g.readline().strip()
                ans_diff = f"Case #{i}: {num_filled_new - num_filled_old}"
                print(ans_diff)
                assert correct_diff == ans_diff, correct_diff + ', ' + ans_diff
                for row in range(N):
                    assert g.readline().strip() == ''.join(grid[row])

            print()
            print('All tests passed!')
            


