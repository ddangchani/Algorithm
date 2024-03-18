def solution(routes):
    answer = 0
    current = -50000 # initialize
    routes.sort(key=lambda x: x[1])
    # search route
    for route in routes:
        if route[0] <= current:
            continue
        else:
            answer += 1
            current = route[1]
            
    return answer