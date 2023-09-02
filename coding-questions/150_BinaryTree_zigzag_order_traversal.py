# Source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Given:
            root: Root of a binary tree
                0 <= size
        Return:
            Zig zag level order traversal of its nodes' values as list of list (by level)
        
        TIME: O(N)
        SPACE: O(N)
        '''
        if root is None:
            return root
        
        res = []
        left_to_right = True
        q = deque([root])
        while len(q) > 0:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if left_to_right:
                res.append(level)
            else:
                res.append(level[::-1])
            left_to_right = not left_to_right
        
        return res
