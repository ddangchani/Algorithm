# 1931 회의실 배정

import sys

N = int(input())
time = [0]
revenue = [0]

for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    revenue.append(p)

res = [0] * (N+2)

# Reverse order DP
for i in range(N, 0, -1):
    ti, pi = time[i], revenue[i]
    if i + ti  >  N+1:
        res[i] = res[i+1]
        continue
    else:
        res[i] = max(res[i+1], res[i+ti] + pi)

print(res[1])


