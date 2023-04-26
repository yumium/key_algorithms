# Source: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # DFS approach
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Given:
            root: Root of tree
                Tree can be empty
                0 <= # nodes <= 100
                -100 <= Node.val <= 100
        Return:
            A list of nodes on right side from top to bottom
        '''
        # TIME: O(N)
        # SPACE: O(N)

        if root is None:
            return []

        res = []
        self.addNode(root, 0, res)

        return res

    def addNode(self, node, level, res):
        if len(res)-1 < level:
            res.append(node.val)
        else:
            res[level] = node.val
        
        if node.left:
            self.addNode(node.left, level+1, res)
        if node.right:
            self.addNode(node.right, level+1, res)

    # BFS approach
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Given:
            root: Root of tree
                Tree can be empty
                0 <= # nodes <= 100
                -100 <= Node.val <= 100
        Return:
            A list of nodes on right side from top to bottom
        '''
        if root is None:
            return []

        res = []  # One node for each level in increasing order, storing right-most node for that level discovered so far
        cur_lvl = -1
        q = [(root, 0)]
        while len(q) > 0:
            n, lvl = q.pop()
            if lvl > cur_lvl:
                res.append(n.val)
                cur_lvl = lvl
            else:
                res[-1] = n.val
            
            if n.left:
                q.insert(0, (n.left, lvl+1))
            if n.right:
                q.insert(0, (n.right, lvl+1))

        return res