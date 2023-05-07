# BFS example code

graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

from collections import deque

deq = deque([1])
visited = [False] * len(graph)
visited[1] = True

while deq:
    i = deq.popleft()
    print(i, end=' ')
    for j in graph[i]:
        if not visited[j]:
            deq.append(j)
            visited[j] = True

