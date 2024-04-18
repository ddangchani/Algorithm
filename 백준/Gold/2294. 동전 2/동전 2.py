# 동전 2

## n kinds of coins > make value=k with the smallest number of coins
## k : 1e5 > DP possible

import sys

n, k = map(int, sys.stdin.readline().split())
coins = list(set([int(sys.stdin.readline()) for _ in range(n)]))
coins.sort()
INF = int(1e9)
dp = [INF] * (k+1)
dp[0] = 0

for c in coins:
    for i in range(c,k+1):
        dp[i] = min(dp[i-c] + 1, dp[i])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
