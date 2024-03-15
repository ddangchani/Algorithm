# Coin 1
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

# dp = [[0] * (k + 1) for _ in range(n+1)]

# # dp[i][j] : i번째 동전까지 사용하여 j원을 표현하는 경우의 수


# for i in range(1, n+1):
#     for j in range(1, k+1):
#         if j < coins[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
        
#         if coins[i-1] == j:
#             dp[i][j] += 1

# print(dp[-1][-1])

# 2D DP : memory over!

# 1D DP solve

dp = [0] * (k+1)

for c in coins:
    for j in range(c, k+1):
        if c == j:
            dp[j] += 1
        dp[j] = dp[j] + dp[j-c]

print(dp[-1])