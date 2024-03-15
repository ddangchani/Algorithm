N = int(input())
ls = list(map(int, input().split()))

dp = [1] * N # initialize

for i in range(N):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
