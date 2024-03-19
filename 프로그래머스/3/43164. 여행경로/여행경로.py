# DFS!
from collections import defaultdict
from itertools import chain

def solution(tickets):
    # to graph dict
    graph = defaultdict(list)
    # graph
    for idx, ticket in enumerate(tickets):
        graph[ticket[0]].append((ticket[1], idx))
    for city in graph:
        graph[city].sort(key=lambda x: x[0])
        
    visited = [False] * len(tickets) # 티켓의 사용여부!
    ans_len = len(tickets) + 1
    result = []
    
    def dfs(city, path):
        if len(path) == ans_len:
            result.append(path.copy()) 
            # important! copy > not to overwrite at pop
            return
        for new_city, ticket_num in graph[city]:
            if visited[ticket_num]: # 사용한 티켓
                continue
            visited[ticket_num] = True
            path.append(new_city)
            dfs(new_city, path)
            # backtrack!
            path.pop()
            visited[ticket_num] = False
            
    dfs('ICN', ['ICN'])
    
    
    return result[0]