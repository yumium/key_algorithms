# Source: Meta Preparation Hub -> General Engineer -> Arrays

def are_they_equal(array_a, array_b):
  # Write your code here
  assert(len(array_a) == len(array_b))
  
  return sorted(array_a) == sorted(array_b)