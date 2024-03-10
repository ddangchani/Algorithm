# 1753 : Dijkstra

from heapq import heappush, heappop
import sys

N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
graph_rev = [[] for _ in range(N+1)]

# Save graph
for _ in range(M): # M : number of directional edges
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])
    graph_rev[v].append([u,w])


# Dijkstra algorithm
def dijkstra(start, graph):
    dist = [int(1e9)] * (N+1)
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, node = heappop(q)
        if dist[node] < d:
            continue
        for g in graph[node]:
            cost = d + g[1]
            if cost < dist[g[0]]:
                dist[g[0]] = cost
                heappush(q, (cost, g[0]))

    return dist
    
# N to X
n_to_x = dijkstra(X, graph_rev)

# X to N
x_to_n = dijkstra(X, graph)

ans = [x + y for x, y in zip(x_to_n, n_to_x)]

print(max(ans[1:]))