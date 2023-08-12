# Source: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Given:
            root: Root node of tree
                values in the tree are integers (can be negative)
        Return:
            Path sum of maximum path in the tree (paths are non-empty, at least 1 node)
            Path sum is the sum of nodes in the path

        obs:
        - Shape of path in tree:
            -> going up then going down the other child, either can be empty
            -> this is the same as going down on both children from a node
        '''
        return self.maxPathSumAtNode(root)[0]


    def maxPathSumAtNode(self, node):
        '''
        Returns (max_path_in_subtree, max_path_at_node) where
            max_path_in_subtree is the maximum path sum of paths within the subtree rooted at `node`
            max_path_from_node is the maximum path sum from `node` down to a child
        '''
        max_path_from_node = node.val  # maximum path from `node` down to a child
        max_path_at_node = node.val  #  maximum path in subtree containing `node`
        candidate_paths = []

        if node.left is not None:
            max_path_in_left, max_path_from_left = self.maxPathSumAtNode(node.left)
            max_path_from_node = max(max_path_from_node, node.val + max_path_from_left)
            max_path_at_node += max(0, max_path_from_left)
            candidate_paths.append(max_path_in_left)

        if node.right is not None:
            max_path_in_right, max_path_from_right = self.maxPathSumAtNode(node.right)
            max_path_from_node = max(max_path_from_node, node.val + max_path_from_right)
            max_path_at_node += max(0, max_path_from_right)
            candidate_paths.append(max_path_in_right)
        
        candidate_paths.append(max_path_at_node)
        max_path_in_subtree = max(candidate_paths)

        return (max_path_in_subtree, max_path_from_node)




    

