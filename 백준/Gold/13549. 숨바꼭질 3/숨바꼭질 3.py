# 13549

import sys
from heapq import heappop, heappush

N, K = map(int, sys.stdin.readline().split())

# dijkstra algorithm?
distance = [int(1e9)] * 100001

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heappop(q)
        if distance[now] < d:
            continue
        new_nodes = [(now * 2, 0), (now - 1, 1), (now + 1, 1)]
        for new, t in new_nodes:
            cost = d + t
            if 0 <= new <= 100000:
                if cost < distance[new]:
                    distance[new] = cost
                    heappush(q, (cost, new))
    
dijkstra(N)

print(distance[K])