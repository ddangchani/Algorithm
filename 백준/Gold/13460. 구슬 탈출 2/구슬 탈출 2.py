# 구슬 탈출 2 > BFS problem

import sys
from collections import deque
from copy import deepcopy
N, M = map(int,sys.stdin.readline().split())
array = [sys.stdin.readline().strip() for _ in range(N)]

for i in range(N):
    if 'R' in array[i]:
        red = [array[i].index('R'),i]
        array[i] = array[i].replace("R",".")
    if 'B' in array[i]:
        blue = [array[i].index('B'),i]
        array[i] = array[i].replace("B",".")
    if 'O' in array[i]:
        hole = [array[i].index('O'),i]

coord = {'r':red, 'b':blue}
                
def move(coordinates, d, i):
    coord = deepcopy(coordinates) # 본래 좌표 훼손 방지
    # d(direction) : 가로 0, 세로 1 / i(increasing) : 증가 1, 감소 -1
    if (coord['r'][d] - coord['b'][d])*i >= 0:
        first, second = 'r', 'b'
    else:
        first, second = 'b', 'r'

    while True: # first 구슬
        coord[first][d] += i
        if coord[first] == hole: # 구멍에 빠짐
            break
        elif array[coord[first][1]][coord[first][0]] == "#": # 벽에 부딪힘
            coord[first][d] -= i
            break

    while True: # second 구슬
        coord[second][d] += i
        if coord[second] == hole:
            break
        elif coord[second] == coord[first] and coord[second] != hole:
            coord[second][d] -= i
            break
        elif array[coord[second][1]][coord[second][0]] == "#":
            coord[second][d] -= i
            break
    
    return coord

deq = deque({})
deq.append(coord)
array_cnt = [[[[0]*N for _ in range(M)] for __ in range(N)] for ___ in range(M)] # 두 구슬 위치 count
array_cnt[coord['r'][0]][coord['r'][1]][coord['b'][0]][coord['b'][1]] = 1

while deq:
    coord = deq.popleft()
    xr, yr = coord['r']
    xb, yb = coord['b']
    moved = []
    
    for d,i in [[0,1],[0,-1],[1,1],[1,-1]]:
        move_coord = move(coord,d,i)
        moved.append(deepcopy(move_coord))

    for m in moved:
        nxr, nyr = m['r']
        nxb, nyb = m['b']
        if (m['b'] != hole) and (array_cnt[nxr][nyr][nxb][nyb] == 0): # 파란공 빠진경우 제외
            if (m['r'] == hole):
                array_cnt[nxr][nyr][nxb][nyb] = array_cnt[xr][yr][xb][yb] + 1
            else:
                array_cnt[nxr][nyr][nxb][nyb] = array_cnt[xr][yr][xb][yb] + 1
                deq.append(m)

ls = sum(array_cnt[hole[0]][hole[1]], [])
ls_cnt = [i for i in ls if i>0] # 0이 아닌 원소들만

if ls_cnt:
    if min(ls_cnt) > 11:
        print(-1)
    else:
        print(min(ls_cnt)-1)
else:
    print(-1)