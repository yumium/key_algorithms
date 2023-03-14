# Source: Meta Preparation Hub -> General Engineer -> Trees

def visible_nodes(root):
  # Write your code here
  # Return the height of the tree at `root`. Returns 0 if the tree is empty.
  if root == None:
    return 0
  
  lh = visible_nodes(root.left)
  rh = visible_nodes(root.right)
  
  return 1 + max(lh,rh)

def visible_nodes_2(root):
  max_level = 0
  q = [(root,1)]
  left_most_nodes = []
  
  while len(q) > 0:
    n, l = q.pop()
    if l > max_level:
      left_most_nodes.append(n.val)
      max_level = l
    if n.left:
      q.insert(0, (n.left,l+1))
    if n.right:
      q.insert(0, (n.right,l+1))
      
  print(left_most_nodes)
  return max_level