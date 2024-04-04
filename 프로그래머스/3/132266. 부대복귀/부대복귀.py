# Note : length of all roads equal > BFS
from collections import deque

def solution(n, roads, sources, destination):
    # Generate graph
    graph = [[] for _ in range(n+1)]
    for edge in roads:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0] * (n+1)
    ans_ls = [-1] * (n+1)
    visited[destination] = 1
    ans_ls[destination] = 0
    
    q = deque()
    q.append([destination,0])
    while q:
        node, l = q.popleft()
        for u in graph[node]:
            if not visited[u]:
                visited[u] = 1
                ans_ls[u] = l+1
                q.append([u, l+1])
    
    return [ans_ls[s] for s in sources]