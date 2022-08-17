# 테트로미노
import sys
N, M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_value = 0
for x in range(M):
    for y in range(N):
