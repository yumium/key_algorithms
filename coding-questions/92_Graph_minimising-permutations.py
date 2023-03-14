# Source: Meta Preparation Hub -> General Engineer -> Graphs

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def is_sorted(arr):
  assert len(arr) > 0
  for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
      return False
  return True

def swaps(arr):
  # Return a list of permutations of `arr` that is 1 subarray reverse away
  # res = []
  for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
      # res.append(swap_subarray(arr, i, j))
      yield swap_subarray(arr, i, j)
  # return res

def swap_subarray(arr, i, j):
  # Return arr when arr[i..j] is reversed
  # Pre: 0 <= i < j < len(arr)
  rev = arr[i:j+1]
  rev.reverse()
  return arr[:i] + rev + arr[j+1:]
  
def minOperations(arr):
  # Write your code here
  '''
  Given:
    arr: len(arr) = N; 1 <= N <= 8; arr is a permutation of [1..N]
  Return:
    min # of subarray reverse to sort the array
  '''
  seen = {str(arr)} # seen permutations as strings
  q = [(arr, 0)] # array & min # of swaps to get from arr0
  while len(q) > 0:
    arr, num_swaps = q.pop()
    if is_sorted(arr):
      return num_swaps
    for swap in swaps(arr):
      if str(swap) not in seen:
        seen.add(str(swap))
        q.insert(0, (swap, num_swaps+1))












# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here
  