# 좌표 정렬
import sys
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x,y])
data.sort()
for i in data:
    print(*i)