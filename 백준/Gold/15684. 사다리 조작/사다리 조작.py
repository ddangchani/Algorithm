# Ladder
import sys
from copy import deepcopy

N, M, H = map(int, sys.stdin.readline().split())
ladders = [[0]*(N+1) for _ in range(H+1)] # row = H, column = N
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ladders[a][b] = 1 # connected to the right
    ladders[a][b+1] = 2 # connected to the left 

answer = 1e9

def get_result(ladders):
    for vline in range(1, N+1): # check for each N vertical lines
        res = vline
        for row in ladders:
            if row[res] == 1:
                res += 1
            elif row[res] == 2:
                res -= 1
        if res != vline:
            return False    
    return True

def backtrack(cur_depth, h_start):
    global answer
    # backtrack combination
    if cur_depth > 3:
        return -1

    if get_result(ladders):
        answer = min(answer, cur_depth)
        return

    for h in range(h_start,H+1): # for each hline
        for v in range(1,N): # for each vline
            # installable at (h,v)
            if ladders[h][v] == 0 and ladders[h][v+1] == 0:
                ladders[h][v] = 1
                ladders[h][v+1] = 2
                backtrack(cur_depth=cur_depth+1, h_start=h)
                ladders[h][v] = 0
                ladders[h][v+1] = 0
    return

backtrack(0, 1)

if answer == 1e9:
    print(-1)
else:
    print(answer)