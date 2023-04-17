# Source: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        Given:
            root: Root of a tree as `TreeNode`
                1 <= # nodes <= 1E4
                -2**31 <= Node.val <= 2**31 - 1
        Return:
            True or False on whether the BST is valid

        Proposition:
            Valid BST <-> InOrder traversal of BST is a strictly increasing list
        '''
        last_val = -2**31 - 1

        stack = []
        node = root
        while node or len(stack) > 0:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val <= last_val:
                    return False
                last_val = node.val
                node = node.right
        return True



