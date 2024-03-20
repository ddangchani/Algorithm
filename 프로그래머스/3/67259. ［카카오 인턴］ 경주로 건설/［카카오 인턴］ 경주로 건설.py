# BFS + dp > 다시풀기
from collections import deque

def solution(board):
    N = len(board)
    INF = int(1e9)
    # 3D list generate >> for 2x !!!
    dp = [[[INF] * 4 for a in range(N)] for _ in range(N)] # dp[y][x] : minimum cost in direction(down, right, up, left)
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    # Initialize
    q = deque()
    for i in range(4):
        dp[0][0][i] = 0
    if not board[0][1]: # (1,0) : right one
        q.append([1,0,100,1])
        dp[0][1][1] = 100
    if not board[1][0]: # (0,1) : bottom one
        q.append([0,1,100,0])
        dp[1][0][0] = 100
        
    while q:
        x, y, cost, d = q.popleft() # (x,y), current cost, current direction
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if d == i:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
            
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if board[ny][nx]:
                continue
            if new_cost < dp[ny][nx][i]:
                q.append([nx,ny,new_cost, i])
                dp[ny][nx][i] = new_cost
                
    return min(dp[-1][-1])
    
    