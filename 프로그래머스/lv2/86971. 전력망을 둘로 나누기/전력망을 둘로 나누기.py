from copy import copy

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        

def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        wires_i = copy(wires)
        del wires_i[i]
        graph = [[] for _ in range(n+1)]
        for x, y in wires_i:
            graph[x].append(y)
            graph[y].append(x)

        visited = [0] * (n+1)
        
        dfs(graph, 1 ,visited)
        
        n1 = sum(visited)
        n2 = n - n1
        
        answer.append(abs(n1-n2))
        
    return min(answer)