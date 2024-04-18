# Tile(G4)

N = int(input())
dp = [0] * 16
dp[0] = 1
dp[1] = 3

if N % 2 == 1: ## Edge : if N is odd > impossible!
    print(0)
else:
    for k in range(2, N//2 + 1):
        # Formula : dp[i] = 3 * dp[i-1] + 2 * dp[i-2] + ... + 2 * dp[0]
        ## equiv to : dp[i]-dp[i-1] = 3 * dp[i-1] - dp[i-2]
        dp[k] = 4 * dp[k-1] - dp[k-2]
    print(dp[N//2])