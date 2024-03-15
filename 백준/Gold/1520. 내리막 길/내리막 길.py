import sys
sys.setrecursionlimit(int(1e6))

#  M * N <= 250000 >> overTime

nrow, ncol = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(nrow)]
dp = [[-1] * ncol for _ in range(nrow)]
# dp[y][x] : (x,y) 에서 목적지까지의 경우의 수

dx, dy = [1,-1,0,0], [0,0,1,-1]

def dfs(x, y):
    if dp[y][x] != -1:
        return dp[y][x]
    
    # 방문한 적이 없는 경우

    cnt = 0 # 0도 경우의 수에 포함되므로 dp를 -1로 initialize
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= ncol or ny < 0 or ny >= nrow:
            continue
        if ls[ny][nx] < ls[y][x]:
            cnt += dfs(nx, ny)

    dp[y][x] = cnt

    return dp[y][x]

dp[-1][-1] = 1 # 역순으로 탐색하므로 최종 지점의 dp=1
dfs(0,0)
print(dp[0][0])