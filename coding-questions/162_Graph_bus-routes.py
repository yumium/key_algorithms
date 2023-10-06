# https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        '''
        Given:
            routes: List of bus routes
            source: Source stop
            target: Target stop
                0 <= source, target, routes[i][j] < 1E6
                sum(len(routes[i])) <= 1E5
                1 <= len(routes[i]) <= 1E5
                1 <= len(routes) <= 500
                All values in routes[i] are unique
        Return:
            Least # of buses to take to get from `source` to `target`. Return -1 if impossible

        Obs:
        - Least # of buses is 0, iff source = target
        '''
        if source == target:
            return 0

        graph = self.buildGraph(routes)

        ss = set()
        ts = set()
        for i in range(len(routes)):
            if source in routes[i]: ss.add(i)
            if target in routes[i]: ts.add(i)

        curlvl = 1
        q = list(ss)
        while len(q) > 0:
            for _ in range(len(q)):
                i = q.pop()
                if i in ts:
                    return curlvl
                for j in graph[i]:
                    if j not in ss:
                        ss.add(j)
                        q.insert(0,j)
            curlvl += 1

        return -1

    def buildGraph(self, routes):
        routes = [set(route) for route in routes]
        graph = {i: set() for i in range(len(routes))}
        for i in range(len(routes)):
            for j in range(i+1, len(routes)):
                if len(routes[i] & routes[j]) > 0:
                    graph[i].add(j)
                    graph[j].add(i)

        return graph

