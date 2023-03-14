def dfs(graph,s):
    seen = set()
    visit(graph,s,seen)
    for node in graph.keys():
        if node not in seen:
            visit(graph,node,seen)

def visit(graph,node,seen):
    seen.add(node)
    for v in graph[node]:
        if v not in seen:
            visit(graph,v,seen)
    print(node)

def bfs(graph, s):
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