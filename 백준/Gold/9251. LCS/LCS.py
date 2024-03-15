# Longest common subsequence (LCS)
w1 = list(input())
w2 = list(input())

# 2D - DP!

dp = [[0] * (len(w2)+1) for _ in range(len(w1)+1)]

# dp[i][j] = w1의 i번째 문자, w2의 j번째 문자까지 이용한 경우의 LCS


for i in range(1, len(w1) + 1):
    for j in range(1, len(w2) + 1):
        if w1[i-1] != w2[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        else: # w1[i-1] == w2[j-1]
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)

print(dp[-1][-1])