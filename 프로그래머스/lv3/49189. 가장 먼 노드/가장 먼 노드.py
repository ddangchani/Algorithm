import heapq

def dijkstra(n, start, graph):
    distance = [1e9] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
                
    return distance
    

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for v in edge:
        a, b = v
        graph[a].append(b)
        graph[b].append(a)
        
    distance = dijkstra(n, 1, graph)[1:]
    
    max_dist = max(distance)
    
    
    return distance.count(max_dist)