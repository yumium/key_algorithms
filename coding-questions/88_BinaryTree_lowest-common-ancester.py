# Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Given:
            root, p, q: Treenodes, all non-null. p != q. p and q both in tree.
                All values of the tree are unique, -1E9 <= Node.val <= 1E9
                2 <= size of tree <= 1E5
        Return:
            The TreeNode that is the LCA of the 2 nodes

        ! A node is an ancestor of itself
        '''
        return self.containPAndQ(root, p, q)[2]

    def containPAndQ(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Return: (hasP, hasQ, LCA/None)
        '''
        if root is None:
            return (False, False, None)

        hasPL, hasQL, LCAL = self.containPAndQ(root.left, p, q)
        if LCAL is not None:
            return (True, True, LCAL)

        hasPR, hasQR, LCAR = self.containPAndQ(root.right, p, q)
        if LCAR is not None:
            return (True, True, LCAR)
        
        if hasPL and hasQR or hasPR and hasQL:
            return (True, True, root)
        
        hasP = hasPL or hasPR or root.val == p.val
        hasQ = hasQL or hasQR or root.val == q.val
        if hasP and hasQ:
            return (True, True, root)
        else:
            return (hasP, hasQ, None)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Given:
            root, p, q: Treenodes, all non-null. p != q. p and q both in tree.
                All values of the tree are unique, -1E9 <= Node.val <= 1E9
                2 <= size of tree <= 1E5
        Return:
            The TreeNode that is the LCA of the 2 nodes

        ! A node is an ancestor of itself
        '''
        if root in [None, p, q] return root
        left = self.lowestCommonAncester(root.left, p, q)
        right = self.lowestCommonAncester(root.left, p, q)
        return root if left and right else left or right








