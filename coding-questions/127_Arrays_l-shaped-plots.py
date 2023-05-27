# Google Kickstart: 2021 - Round A

import pandas as pd
import logging

def l_segments(R, C, grid):
    '''
    Given:
        R: # of rows in grid
            1 <= R <= 1000
        C: # of columns in grid
            1 <= C <= 1000
        grid: A matrix of shape (R,C) of bits
    Return:
        # of L-shape in grid
        
    Obs:
    - To make searching canonical, we can exhaust all possible longer sticks within the pair
    - Or perhaps we can search from vertical and, for each, try horizontal
        - One way to search vertical is to go from left to right,
            Then for each try head from top to bottom
            And with each head try adding one block at a time
        - Each state, we keep track of all the horizontal lines coming out of it and their count
            - We can precompute this
    
        TIME: R^3 * C
        SPACE: O(R)
        
        - Make R the smaller of the 2 dimensions
        - Repeated work might be the R^2 search
    - Try intersections
        TIME: # intersections * (C + R)
        SPACE: O(1)
    - Further reduction => the (C + R) time loop can be reduced
        - 
    - Precompute segments for each row and col
        - TIME: O(R*C)
        - SPACE: O(R*C)
    '''
    num_ls = 0
    
    rows, cols = build_matrix(R, C, grid)
    for i in range(R):
        for j in range(C):
            if rows[i][j] is not None and cols[i][j] is not None:
                t, b = cols[i][j]
                l, r = rows[i][j]

                increment = count_ls(i-t+1, b-i+1, j-l+1, r-j+1)
                num_ls += increment
                # logging.info(f'Increment {increment} for position ({i},{j})')
    
    return num_ls


def build_matrix(R, C, grid):
    rows = make_grid(R,C)
    cols = make_grid(R,C)
    
    # rows
    for i in range(R):
        segment = None
        for j in range(C):
            if grid[i][j] == 0:
                segment = None
            else:
                if segment is None:
                    segment = [j,j]
                else:
                    segment[1] = j
            rows[i][j] = segment
    
    # cols
    for j in range(C):
        segment = None
        for i in range(R):
            if grid[i][j] == 0:
                segment = None
            else:
                if segment is None:
                    segment = [i,i]
                else:
                    segment[1] = i
            cols[i][j] = segment
            
    return (rows, cols)
            
            
def make_grid(R, C):
    return [[None]*C for i in range(R)]


def count_ls(top, bottom, left, right):
    count = 0
    if top > 1:
        if left >= 2: count += min(top, left//2) - 1
        if right >= 2: count += min(top, right//2) - 1
    if bottom > 1:
        if left >= 2: count += min(bottom, left//2) - 1
        if right >= 2: count += min(bottom, right//2) - 1

    if top >= 4:
        if left >= 2: count += min(top//2, left) - 1
        if right >= 2: count += min(top//2, right) - 1
    if bottom >= 4:
        if left >= 2: count += min(bottom//2, left) - 1
        if right >= 2: count += min(bottom//2, right) - 1

    return count

INPUT = 'input.txt'
ANS = 'ans.txt'

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    with open('input.txt', 'r') as f:
        with open('ans.txt', 'r') as g:
            t = int(f.readline())
            for i in range(1, t+1):
                [R,C] = [int(s) for s in f.readline().split(' ')]
                grid = []
                for j in range(R):
                    grid.append([int(s) for s in f.readline().split(' ')])
                # print("Case #{0}: {1}".format(i, l_segments(R, C, grid)))
                out = "Case #{0}: {1}".format(i, l_segments(R, C, grid))
                correct = g.readline().strip()
                print(out)
                assert out == correct, f'Algorithm output {out}, correct output {correct}'

if __name__ == '__main__':
    main()