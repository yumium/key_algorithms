# Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Given:
            root: root node of BST
            k: k-th smallest value (1-indexed)
                1 <= k <= n <= 1E4
                0 <= Node.val <= 1E4
                Assume all nodes are unique
        Return: 
            value of the k-th smallest node in BST
        
        TIME: O(k)
        SPACE: O(H)
        '''
        stack = []
        curNode = root
        next_node = 1  # Index of next node (from smallest to biggest)
        while curNode or len(stack) > 0:
            if curNode:
                stack.append(curNode)
                curNode = curNode.left

            else:
                curNode = stack.pop()
                if next_node == k:
                    return curNode.val
                next_node += 1
                curNode = curNode.right
        