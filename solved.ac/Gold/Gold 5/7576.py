# 토마토 easy
import sys
from collections import deque

M, N = map(int,sys.stdin.readline().split())
deq = deque([])
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            deq.append([j,i])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0<=nx<M) and (0<=ny<N) and (matrix[ny][nx]) == 0:
            matrix[ny][nx] = matrix[y][x] + 1 # 진행도를 원소에 반영!
            deq.append([nx,ny])
isbreak = False
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            isbreak = True
            break
    if isbreak:
        break
    cnt = max(cnt, max(i))

if not isbreak:
    print(cnt - 1)