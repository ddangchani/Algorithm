# Dijkstra
from heapq import heappop, heappush
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append([v, cost])

start, finish = map(int,sys.stdin.readline().split())

# heapq
q = []
distance = [int(1e9)] * (N+1)
heappush(q, (0, start))

while q:
    d, now = heappop(q)
    if distance[now] < d: # already visited
        continue
    for v, cost in graph[now]:
        cost_new = d + cost
        if cost_new < distance[v]:
            distance[v] = cost_new
            heappush(q, (cost_new, v))

print(distance[finish])