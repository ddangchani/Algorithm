# 토마토(3D)
import sys
from collections import deque
M, N, H = map(int,sys.stdin.readline().split())
deq = deque([])
array = []
for _ in range(H):
    ls = []
    for __ in range(N):
        ls.append(list(map(int,sys.stdin.readline().split())))
    array.append(ls)
for h in range(H):
    for n in range(N):
        for m in range(M):
            if array[h][n][m] == 1:
                deq.append([m,n,h])

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while deq:
    x, y, z = deq.popleft()
    for i in range(6):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
        if (0<=nx<M) and (0<=ny<N) and (0<=nz<H) and array[nz][ny][nx]==0:
            array[nz][ny][nx] = array[z][y][x] + 1
            deq.append([nx,ny,nz])

cnt = 0
isbreak = False
for i in array:
    for j in i:
        if 0 in j:
            isbreak = True
            print(-1)
            break
        else:
            cnt = max(cnt, max(j))

    if isbreak:
        break

if not isbreak:
    print(cnt - 1)