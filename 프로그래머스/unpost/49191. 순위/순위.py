
def solution(n, results):
    graph = [[0]*n for _ in range(n)]
        
    for result in results:
        win, lose = result
        graph[win-1][lose-1] = 1
    
    # Floyd-Warshall
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if (graph[j][l] == 0) and (graph[j][k] == 1 and graph[k][l] == 1):
                    graph[j][l] = 1
                    
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if (graph[j][l] == 0) and (graph[j][k] == 1 and graph[k][l] == 1):
                    graph[j][l] = 1
    
    answer = [0] * n
    for i in range(n):                  
        for j in range(n):
            if graph[i][j] == 1:
                answer[i] += 1
                answer[j] += 1
    
    return answer.count(n-1)