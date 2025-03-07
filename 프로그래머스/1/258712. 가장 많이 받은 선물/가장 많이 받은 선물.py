def solution(friends, gifts):
    name_dict = dict()
    for i,n in enumerate(friends):
        name_dict[n] = i
    
    N = len(friends)
    table = [[0] * N for _ in range(N)]
    
    for g in gifts:
        _from, _to = map(name_dict.get, g.split(' '))
        table[_from][_to] += 1
    
    present_index = [sum(table[i]) - sum([table[r][i] for r in range(N)]) for i in range(N)] # 선물 지수
    
    # Calculate result
    result = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if table[i][j] > table[j][i]: # i to j
                result[i] += 1
            elif table[i][j] == table[j][i]:
                if present_index[i] > present_index[j] :
                    result[i] += 1
                elif present_index[i] < present_index[j] :
                    result[j] += 1
            else:
                result[j] += 1            
                
    
    return max(result)