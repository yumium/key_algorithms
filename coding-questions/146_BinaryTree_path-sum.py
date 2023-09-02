# Source: https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        Given:
            root: Root of a binary tree
                0 <= # of nodes
                -1000 <= Node.val <= 1000
            targetSum: Sum for root to leaf path
                -1000 <= targetSum <= 1000
        Return:
            A list of path values from root to a leaf that equals `targetSum`

        TIME: O(N)
        SPACE: O(1)
        '''
        if not root:
            return []

        if not root.left and not root.right:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []

        paths = self.pathSum(root.left, targetSum-root.val) + self.pathSum(root.right, targetSum-root.val)
        return [[root.val] + path for path in paths]
    
