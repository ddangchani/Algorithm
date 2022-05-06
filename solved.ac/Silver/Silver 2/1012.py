# 유기농 배추
import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())
# DFS function
def dfs(x,y): # 각 좌표에서 시작하는 DFS
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (0<=new_x<N) and (0<=new_y<M):
            if matrix[new_x][new_y] == 1:
                matrix[new_x][new_y] = -1
                dfs(new_x,new_y)

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    matrix = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        m, n = map(int,sys.stdin.readline().split())
        matrix[n][m] = 1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                dfs(i,j)
                cnt += 1
    print(cnt)