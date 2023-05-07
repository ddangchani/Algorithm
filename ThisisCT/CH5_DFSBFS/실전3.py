N, M = map(int, input().split(' '))
graph = [list(map(int, list(input()))) for _ in range(N)]

def dfs(v):
    graph[v[0]][v[1]] = 1 # 첫번째 인덱스가 세로, 두번째 인덱스가 가로

    adj = [[0,1],[0,-1],[-1,0],[1,0]]
    for a in adj:
        adj_v = [x + y for x, y in zip(v, a)]
        
        if (0<=adj_v[0]<=N-1) and (0<=adj_v[1]<=M-1) and (graph[adj_v[0]][adj_v[1]]==0):
            dfs(adj_v)

cnt = 0
for n in range(N):
    for m in range(M):
        if graph[n][m] == 0:
            dfs([n,m])
            cnt += 1
            print([n,m])

print(cnt)