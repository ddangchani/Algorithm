# 1931 회의실 배정

import sys

N = int(input())
ls = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ls.sort(key = lambda x: [x[1],x[0]]) # end point 기준 정렬

cnt = 0

s = e = 0

for _ in range(N):
    ns, ne = ls.pop(0)
    if ns >= e:
        cnt += 1
        s = ns
        e = ne

print(cnt)