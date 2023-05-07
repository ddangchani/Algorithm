# 최소 경로 > BFS!
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

from collections import deque

deq = deque([[0,0]])

while deq:
    v = deq.popleft()
    d = graph[v[0]][v[1]]

    adj = [[1,0],[-1,0],[0,1],[0,-1]]
    for a in adj:
        v_a = [x+y for x, y in zip(v,a)] # new vertex
        if (0<=v_a[0]<=n-1) and (0<=v_a[1]<=m-1) and (graph[v_a[0]][v_a[1]] == 1): # 처음 방문하는 경우 기록
            graph[v_a[0]][v_a[1]] = d + 1
            deq.append(v_a)

print(graph[n-1][m-1])