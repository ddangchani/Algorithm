# Solve again!

import sys
sys.setrecursionlimit(10000)
C, N = map(int, sys.stdin.readline().split())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [int(1e7) for _ in range(C+100)] # point ! : maximum N = 100 thus overing num can be 100
dp[0] = 0

for cost, cust in costs:
    for i in range(cust,C+100):
        dp[i] = min(dp[i - cust] + cost, dp[i])
    

print(min(dp[C:]))