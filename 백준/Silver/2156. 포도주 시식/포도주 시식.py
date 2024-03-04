import sys

N = int(sys.stdin.readline()) # number of glasses

wines = [int(sys.stdin.readline()) for _ in range(N)]

cnt = [0] * 10001

if N >= 1:
    cnt[0] = wines[0]
if N >= 2:
    cnt[1] = wines[0] + wines[1]
if N >= 3:
    cnt[2] = max(wines[0]+wines[1], wines[0]+wines[2], wines[1]+wines[2])
    for i in range(3, N):
        cnt[i] = max(cnt[i-3]+wines[i-1]+wines[i], cnt[i-2]+wines[i], cnt[i-1])

print(cnt[N-1])