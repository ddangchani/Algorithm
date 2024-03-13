# Solve again!

import sys
sys.setrecursionlimit(10000)
C, N = map(int, sys.stdin.readline().split())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = [int(1e7) for _ in range(C+100)] # point ! : maximum N = 100 thus overing num can be 100
dp[0] = 0

for cost, cust in costs: # 현재 도시에서 손님을 받는 경우
    for i in range(cust,C+100): # point ! : C+100까지만 계산해도 충분하다. 왜냐하면, 최대 100명의 손님이 있으므로, 100명을 넘어가는 경우는 고려할 필요가 없다.
        dp[i] = min(dp[i - cust] + cost, dp[i]) # i번째 손님까지의 최소비용 update
    

print(min(dp[C:]))