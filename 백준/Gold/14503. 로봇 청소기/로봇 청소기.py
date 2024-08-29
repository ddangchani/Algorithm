# 1931 회의실 배정

import sys

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# d : direction (0:North, 1:East, 2:South, 3:West)
back_dict = {
    0 : [1,0],
    1 : [0,-1],
    2 : [-1,0],
    3 : [0, 1]
}

front_dict = {
    0 : [-1, 0],
    1 : [0,1],
    2 : [1,0],
    3 : [0, -1]
}

rotate_dict = {0 : 3, 1 : 0, 2 : 1, 3: 2}

dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def second_cond(r,c):
    for dr, dc in dxy:
        nr, nc = r + dr, c + dc
        if nr >= 0 and nc >= 0 and nr < N and nc < M:
            if room[nr][nc] == 0:
                return False

    return True


def robot(r,c,d):
    cnt = 0
    while True:
        # 현재 칸 청소 X : 현재 칸 청소
        if room[r][c] == 0:
            room[r][c] = 2
            cnt += 1
        # 2
        if second_cond(r, c): # 주변 빈칸 없는 경우
            br, bc = [sum(x) for x in zip([r,c], back_dict[d])]
            if (0<=br<N) and (0<=bc<M) and (room[br][bc] == 2): # 후진가능여부(청소구역인 경우는 가능)
                r, c = br, bc
            else:
                return cnt
        # 3
        else:
            d = rotate_dict[d]
            fr, fc = [sum(x) for x in zip([r,c], front_dict[d])]
            if (0<=fr<N) and (0<=fc<M):
                if room[fr][fc] == 0:
                    r, c = fr, fc

print(robot(r,c,d))