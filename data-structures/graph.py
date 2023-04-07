class Graph:
    def __init__(self):
        pass

    @classmethod
    def dfs(cls, graph,s):
        seen = set()
        cls.visit(graph,s,seen)
        for node in graph.keys():
            if node not in seen:
                cls.visit(graph,node,seen)

    @classmethod
    def visit(cls,graph,node,seen):
        seen.add(node)
        for v in graph[node]:
            if v not in seen:
                cls.visit(graph,v,seen)
        print(node)

    @classmethod
    def bfs(cls, graph, s):
        seen = {s}      # Or an array d containing distances, initialised at inf.
        q = FIFOqueue(len(graph))
        q.enqueue(s)
        while not q.isEmpty():
            node = q.dequeue()
            print(node)
            for v in graph[node]:
                if v not in seen:
                    seen.add(v) # REMEMBER THIS
                    q.enqueue(v)