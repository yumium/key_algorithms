# Source: Meta Preparation Hub -> General Engineer -> Arrays

def findSignatureCounts(arr):
  # Write your code here
  n = len(arr)
  res = [None]*n
  
  for i in range(0,n):
    # Skip if student already in previous ring
    if res[i] is not None:
      continue
    
    # Follow the ring
    students_in_ring = [i] # indices (0-based)
    next = arr[i]
    while next != i+1:
      students_in_ring.append(next-1)
      next = arr[next-1]
      
    # Update for students in ring
    size = len(students_in_ring)
    for j in students_in_ring:
      res[j] = size
      
  return res
