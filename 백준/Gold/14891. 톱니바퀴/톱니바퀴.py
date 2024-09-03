# 톱니바퀴

import sys
from collections import defaultdict, deque

# Data input
ls = [list(map(int, list(input()))) for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

def clockwise(i):
    new = ls[i].pop()
    ls[i] = [new] + ls[i]

def counterclockwise(i):
    new = ls[i].pop(0)
    ls[i] =  ls[i] + [new]

def check_connected():
    indices = [[[0,2],[1,6]], [[1,2],[2,6]],[[2,2],[3,6]]]
    res = defaultdict(list)
    for idx, comb in enumerate(indices):
        i1, v1 = comb[0]
        i2, v2 = comb[1]
        if ls[i1][v1] != ls[i2][v2]:
            res[idx].append(idx+1)
            res[idx+1].append(idx)
    return res # return the index of the connection (S vs N)

def bfs_search(graph, start, d):
    visited = [0,0,0,0]
    visited[start] = d
    q = deque([[start,d]])
    while q:
        c_idx, c_d = q.popleft()
        for n_idx in graph[c_idx]:
            if not visited[n_idx]:
                visited[n_idx] = -c_d
                q.append([n_idx, -c_d])

    return visited

def rotate(visited): # index and direction (1:clockwise, -1:counterclockwise)
    for idx, d in enumerate(visited):
        if d == 1:
            clockwise(idx)
        elif d == -1:
            counterclockwise(idx)
        else:
            pass


for start, d in rotation:
    start -= 1
    graph = check_connected() # check current connection state
    visited = bfs_search(graph, start, d)
    rotate(visited)

print(sum([int(ls_i[0] == 1)*(2**i) for i, ls_i in enumerate(ls)])) # final score
