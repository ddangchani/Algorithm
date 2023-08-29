def dfs(v, computers, visited):
    visited[v] = 1
    for idx,val in enumerate(computers[v]):
        if val == 1 and visited[idx] == 0:
            dfs(idx, computers, visited)
    

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for idx, val in enumerate(visited):
        if val == 0:
            dfs(idx, computers, visited)
        else:
            continue
        
        answer += 1
    return answer