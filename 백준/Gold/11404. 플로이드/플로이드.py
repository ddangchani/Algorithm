import sys

# Floyd-Warshall
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
# DP table
dp = [[int(1e9)] * (n+1) for _ in range(n+1)] 
# dp[i][j] : minimum cost of path from node i to node j

# Initialize
for _ in range(m):
    i, j, cost = map(int, sys.stdin.readline().split())
    dp[i][j] = min(cost, dp[i][j]) # 여러 노선이 있을 때 생각!

for k in range(1, n+1): # stopover
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            dp[i][j] = 0
        if dp[i][j] == int(1e9):
            dp[i][j] = 0

# print
for i in range(1, n+1):
    print(*dp[i][1:])