# Source: https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # TIME: O(N)
        # SPACE: O(N)

        # Dictionary: node -> set of neighbours
        graph = {i: set() for i in range(n)}
        for e in edges:
            a, b = e[0], e[1]
            graph[a].add(b)
            graph[b].add(a)

        leaves = {i for i in range(n) if len(graph[i]) <= 1}
        nodes_left = n
        # Invariant: `nodes_left` is # of nodes left in subgraph & `leaves` are leaves in subgraph
        while nodes_left > 2:
            new_leaves = set()
            for l in leaves:
                n = graph[l].pop()
                graph[n].remove(l)
                if len(graph[n]) <= 1:
                    new_leaves.add(n)

            nodes_left -= len(leaves)
            leaves = new_leaves

        return list(leaves)


    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Given:
            n: # of nodes in tree
            edges: A list of list (edges)
                1 <= n <= 2E4
                len(edges) = n-1
                nodes are labelled as integers in range [0..N)
        Return:
            A list of all MHT's root labels, return in any order (height = # of edges from root to deepest leaf)

        Obs:
        - The returned list will have at least 1 element

        TIME: O(N * N)
        SPACE: O(N)
        '''
        # Dictionary: node -> set of neighbours
        graph = {i: set() for i in range(n)}
        for e in edges:
            a, b = e[0], e[1]
            graph[a].add(b)
            graph[b].add(a)

        res = []
        min_depth = n
        for i in range(n):
            d = self.findDepth(i, graph)
            if d < min_depth:
                min_depth = d
                res = [i]
            elif d == min_depth:
                res.append(i)

        return res

    def findDepth(self, root, graph):
        cur_depth = 0
        q = [(root, 0)]
        seen = {root}
        while len(q) > 0:
            n, d = q.pop()
            cur_depth = d
            for u in graph[n]:
                if u not in seen:
                    q.insert(0, (u, d+1))
                    seen.add(u)

        return cur_depth