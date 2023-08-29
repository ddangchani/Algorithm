def dfs(node, n_sheep, n_wolf, next_node, info):
    global graph, result
    if info[node] == 0:
        n_sheep += 1
        result = max(result, n_sheep)
    else:
        n_wolf += 1

    if n_wolf >= n_sheep:
        return
    
    next_node.extend(graph[node])
    for g in next_node:
        next_node_g = next_node[:]
        next_node_g.remove(g)
        dfs(g, n_sheep, n_wolf, next_node_g, info)


def solution(info, edges):
    global graph, result
    n = len(info)
    graph = [[] for _ in range(n)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        
    result = 0

    dfs(0, 0, 0, [], info)
        
    return result