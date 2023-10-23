# Source: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        Given:
            root: Root of a binary tree
            target: Target node in binary tree
            k: Integer
                1 <= # of nodes <= 500
                0 <= Node.val <= 500, all values unique, `target` is a node in the tree
                0 <= k <= 1000
        Return:
            Array of values of all nodes that have a distance `k` from target node
                Distance = # of edges in path between start and end nodes
        
        Obs:
        - If k = 0, then return []

        TIME: O(N)
        SPACE: O
        '''
        if k == 0:
            return [target.val]

        graph = self.createGraph(root) # val => neighbours of `val`

        print('done')
        q = [target.val]
        seen = {target.val}
        dist = 0
        # Invariant: q contains nodes that are distance `dist` away from `target`
        while dist < k:
            if len(q) == 0:
                return []

            for _ in range(len(q)):
                n = q.pop()
                for v in graph[n]:
                    if v not in seen:
                        q.insert(0, v)
                        seen.add(v)

            dist += 1
        
        return q

    def createGraph(self, root):
        graph = {}

        stack = [None]
        curNode = root

        while curNode:
            print('here')
            print(curNode.val)
            if curNode.left:
                self.addUndirectedEdge(graph, curNode.val, curNode.left.val)                
            if curNode.right:
                self.addUndirectedEdge(graph, curNode.val, curNode.right.val)                

            if curNode.right:
                stack.append(curNode.right)
        
            if curNode.left:
                curNode = curNode.left
            else:
                curNode = stack.pop()

        return graph

    def addUndirectedEdge(self, graph, s, e):
        if s in graph:
            graph[s].add(e)
        else:
            graph[s] = {e}
        
        if e in graph:
            graph[e].add(s)
        else:
            graph[e] = {s}

sol = Solution()
target = TreeNode(5,
        TreeNode(6),
        TreeNode(2,
            TreeNode(7),
            TreeNode(4)
        )
    )
myTree = TreeNode(3,
    target,
    TreeNode(1,
        TreeNode(0),
        TreeNode(8)
    )
)

