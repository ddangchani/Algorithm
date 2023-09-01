def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    graph[0][0] = 1
    
    for puddle in puddles:
        x, y = puddle
        graph[y-1][x-1] = -1
    
    for y in range(0,n):
        for x in range(0,m):
            if not graph[y][x]:
                if x == 0:
                    graph[y][x] = max(graph[y-1][x],0) % 1000000007
                elif y == 0:
                    graph[y][x] = max(graph[y][x-1],0) % 1000000007
                else:
                    graph[y][x] = (max(graph[y-1][x],0) + max(graph[y][x-1],0)) % 1000000007
                
    
    answer = graph[n-1][m-1]
    return answer