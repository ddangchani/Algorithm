import sys
sys.setrecursionlimit(int(1e6))

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0]* N for _ in range(N)]
visited2 = [[0]* N for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs_normal(q, visited):
    # q : coordinate [x,y]
    x, y = q
    col = graph[y][x]
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if graph[ny][nx] != col : # new color != current color
            continue
        if not visited[ny][nx]:
            dfs_normal([nx, ny], visited)

def dfs_colorblind(q, visited):
    # q : coordinate [x,y]
    x, y = q
    col = graph[y][x]
    visited[y][x] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        nc = graph[ny][nx] # new color
        if (col == 'B' and nc in ['R','G']) or (nc == 'B' and col in ['R','G']):
            continue
        if not visited[ny][nx]:
            dfs_colorblind([nx, ny], visited)


ans_normal = 0
for i in range(N): # x
    for j in range(N): # y
        if not visited[j][i]:
            dfs_normal([i,j], visited)
            ans_normal += 1
ans_cb = 0
for i in range(N): # x
    for j in range(N): # y
        if not visited2[j][i]:
            dfs_colorblind([i,j], visited2)
            ans_cb += 1

print(ans_normal, ans_cb)