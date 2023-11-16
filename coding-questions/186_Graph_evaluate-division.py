# Source: https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Given:
            equations: Array of variable pairs              N
            values: Array of reals                          N
            queries: Array of variable pairs for queries    Q
                1 <= N, Q <= 20
                1 <= len(equations[i][0]), len(equations[i][1]), len(queries[i][0]), len(queries[i][1]) <= 5
                0.0 <= values[i] <= 20.0
                equations/queries[i][0]/[1] consist of lowercase English letters and digits

        Return:
            A list of answers to all queries
            If a variable in `queries` does not exist in `equations`, the query is undefined, return -1
            If answer cannot be determined, return -1

        Assumptions:
            Queries are valid (no division by zero, contradition, divide by itself etc.)

        Ideas/Obs:
            - If query contain variables unknown, return -1
            - Build a graph, where undirected edge is an equation. Query that can be determined are exactly between nodes that are connected
        '''
        res = []
        
        graph, ratios = self.build_graph(equations, values)

        for s, t in queries:
            if s not in graph or t not in graph:
                res.append(-1)
            else:
                seen = {s}
                q = [(s,1)] # (node, s / node)
                while len(q) > 0:
                    n, ratio = q.pop()
                    if n == t:
                        res.append(ratio)
                        break
                    for v in graph[n]:
                        if v not in seen:
                            seen.add(v)
                            q.insert(0, (v, ratio * ratios[(n,v)]))
                else:
                    res.append(-1)
        
        return res

    def build_graph(self, equations, values):
        variables = set()
        for s, t in equations:
            variables.add(s)
            variables.add(t)

        graph = {v: set() for v in variables}
        ratios = {}

        for (s, t), ratio in zip(equations, values):
            graph[s].add(t)
            graph[t].add(s)
            ratios[(s,t)] = ratio
            ratios[(t,s)] = 1 / ratio

        return (graph, ratios)
