def solution(n, costs):
    # Kruskal Algorithm
    parent = list(range(n)) # parent initialization
    costs.sort(key=lambda x : x[2]) 
    answer = 0
    
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x]) ## 경로 압축
        return parent[x]
    
    def union_parent(parent, x, y):
        x = find_parent(parent, x)
        y = find_parent(parent, y)
        if x < y :
            parent[y] = x
        else:
            parent[x] = y
    
    for u, v, cost in costs:
        if find_parent(parent, u) != find_parent(parent, v):
            union_parent(parent, u, v)
            answer += cost
    
    return answer