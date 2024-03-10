# 연구소 14502

# BFS problem, total combination ~= 40000
import sys
from collections import deque
from itertools import combinations, chain
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
empty = [] # empty coordinates
virus = [] # virus coordinates

for x in range(M):
    for y in range(N):
        if graph[y][x] == 2:
            virus.append([x,y])
        elif graph[y][x] == 0:
            empty.append([x,y])
        else:
            pass

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs_safety(walls):
    gr = deepcopy(graph) # copy new graph
    for w in walls:
        gr[w[1]][w[0]] = 1
    deq = deque(virus)
    while deq:
        cx, cy = deq.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i] # new coordinate
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if gr[ny][nx] == 0:
                deq.append([nx, ny])
                gr[ny][nx] = 2
    
    return list(chain(*gr)).count(0) # safety area

# Wall combinations

combs = combinations(empty, 3)

ans = 0
for walls in combs:
    ans = max(ans, bfs_safety(walls))

print(ans)