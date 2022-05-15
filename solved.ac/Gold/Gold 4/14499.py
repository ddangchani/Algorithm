# 주사위 굴리기
import sys
from copy import deepcopy
N, M, y, x, K = map(int, sys.stdin.readline().split())
array = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
commands = list(map(int,sys.stdin.readline().split()))
dice = [[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]] # 전개도 모양
coord = [x,y] # 주사위 바닥이 놓여진 좌표

def move(dxy,coord,dice,array):
    new_array = deepcopy(array)
    new_dice = deepcopy(dice)
    ncoord = [a+b for a,b in zip(coord,dxy)]
    if (0<=ncoord[0]<M) and (0<=ncoord[1]<N):
        if dxy[0] == 0: # 수직방향 움직임
            center = [i[1] for i in new_dice] # 전개도 중앙 열
            if dxy[1] == -1: # 위로 움직임
                center.append(center.pop(0))
            else: # 아래로 움직임
                center.insert(0,center.pop())
            for i,v in enumerate(center):
                new_dice[i][1] = v
        else: # 수평 움직임
            center = deepcopy(dice[1])
            if dxy[0] == 1: # 오른쪽 움직임
                new_dice[3][1] = center.pop()
                center.insert(0,dice[3][1])
            else:
                new_dice[3][1] = center.pop(0)
                center.append(dice[3][1])
            new_dice[1] = deepcopy(center)

        if new_array[ncoord[1]][ncoord[0]] == 0:
            new_array[ncoord[1]][ncoord[0]] = deepcopy(new_dice[3][1])
        else:
            new_dice[3][1] = deepcopy(new_array[ncoord[1]][ncoord[0]])
            new_array[ncoord[1]][ncoord[0]] = 0
        print(new_dice[1][1])
        return ncoord, new_dice, new_array

    else:
        return coord, new_dice, new_array
        
direction = {1:[1,0], 2:[-1,0], 3:[0,-1], 4:[0,1]}

for k in commands:
    dxy = direction[k]
    coord, dice, array = move(dxy, coord, dice, array)