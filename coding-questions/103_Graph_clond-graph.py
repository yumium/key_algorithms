# Source: https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        Given:
            node: A node of the connected, undirected graph
                node.val is unique for every node
                1 <= node.val <= 100
                0 <= # of nodes in graph <= 100
                no repeated edges or self-loops
        Return:
            The same node copied to an identical graph
        '''

        # TIME: O(|V| + |E|)
        # SPACE: O(|V|)

        # Empty graph
        if node is None:
            return None

        # Build dict: val -> orig_node
        orig_nodes = {}
        self.visit(node, orig_nodes)

        # Create new dict: val -> new_node (empty edges)
        new_nodes = {}
        for val in orig_nodes:
            new_nodes[val] = Node(val)

        # Fill in the edges -> go through each node (by value) 
        for val, node in orig_nodes.items():
            if node.neighbors is not None:
                new_nodes[val].neighbors = []
                for u in node.neighbors:
                    new_nodes[val].neighbors.append(new_nodes[u.val])

        # print(new_nodes[node.val].val)
        return new_nodes[1]

    def visit(self, node, orig_nodes):
        orig_nodes[node.val] = node
        for u in node.neighbors:
            if u.val not in orig_nodes:
                self.visit(u, orig_nodes)
        
                    


