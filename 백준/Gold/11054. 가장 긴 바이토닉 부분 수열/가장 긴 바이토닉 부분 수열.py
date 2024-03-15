# Longest bitonic subsequence

N = int(input())
ls = list(map(int,input().split()))
l = len(ls)

# 1 dimensional DP
dp = [1] * l  # dp[i] : i번째 수가 S_k(최대값)이 되는 최대 lbs 길이


# LIS
for i in range(l):
    for s in range(i): # S_k의 왼쪽 파트(작은 수열 카운트)
        if ls[s] < ls[i]:
            dp[i] = max(dp[s] + 1, dp[i])


# LDS
dp2 = [1] * l
for i in range(l-1, -1, -1):
    for b in range(i+1, l):
        if ls[b] < ls[i]:
            dp2[i] = max(dp2[b] + 1, dp2[i])


result = [u + v - 1 for u,v in zip(dp, dp2)]
print(max(result))