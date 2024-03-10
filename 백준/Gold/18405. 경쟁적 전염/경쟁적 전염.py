# 경쟁적 전염
import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, y, x = map(int,sys.stdin.readline().split())

# BFS reverse way? (x, y) to initial points of each K virus
## Take the lowest idx virus if there is equivalence

visited = [[0] * N for _ in range(N)]
ans_list = [10002] * K # corresponds to each virus
deq = deque()

deq.append([x-1, y-1])
if graph[y-1][x-1]:
    ans_list[graph[y-1][x-1]-1] = 0

visited[y-1][x-1] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]

while deq:
    cx, cy = deq.popleft()
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if not visited[ny][nx]:
            deq.append([nx, ny])
            visited[ny][nx] = visited[cy][cx] + 1
            if graph[ny][nx]:
                ans_list[graph[ny][nx]-1] = min(visited[ny][nx], ans_list[graph[ny][nx]-1])

min_time = min(ans_list)

if S >= min_time - 1:
    print(ans_list.index(min_time) + 1)
else:
    print(0)