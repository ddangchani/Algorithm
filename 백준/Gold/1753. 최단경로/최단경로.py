# 1753 : Dijkstra

from heapq import heappush, heappop
import sys

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
dist = [int(1e9)] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])

def dijkstra(start):
    heap = []
    heappush(heap, (0, start)) # initialize
    dist[start] = 0
    while heap:
        d, n = heappop(heap)
        if dist[n] < d: # already visited
            continue
        for g in graph[n]:
            cost = d + g[1]
            if cost < dist[g[0]]:
                dist[g[0]] = cost
                heappush(heap, (cost, g[0]))

dijkstra(start)

for i in dist[1:]:
    print('INF' if i == int(1e9) else i)

