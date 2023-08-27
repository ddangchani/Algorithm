# Dijkstra

import heapq

def dijkstra(start, graph, n):
    q = []
    route = [[] for _ in range(n+1)]
    costs = [1e9] * (n+1)
    heapq.heappush(q, (0, start))
    costs[start] = 0
    route[start].append(start)
    
    while q:
        cost, now = heapq.heappop(q)
        if costs[now] < cost:
            continue
        for i in graph[now]:
            new_cost = cost + i[1]
            if new_cost < costs[i[0]]:
                costs[i[0]] = new_cost
                route[i[0]] = route[now] + [i[0]]
                heapq.heappush(q, (new_cost, i[0]))
    
    for i, r in enumerate(route):
        if i>0:
            route[i].append(i)
    return costs
                
            

def solution(n, s, a, b, fares):
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c,d,f = fare
        graph[c].append([d,f])
        graph[d].append([c,f])
        
    # costs and route
    cost_a = dijkstra(a, graph, n)
    cost_b = dijkstra(b, graph, n)
    cost_s = dijkstra(s, graph, n)
    
    # elementwise sum
    cost_total = [sum(x) for x in zip(cost_a, cost_b, cost_s)] 
        
    return min(cost_total)