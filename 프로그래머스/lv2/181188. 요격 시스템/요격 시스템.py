def solution(targets):
    targets.sort(key=lambda x: [x[1], x[0]]) # end point 기준으로 정렬!!1

    answer = 0
    s = e = 0
    for s_new, e_new in targets:
        if s_new >= e:
            answer += 1
            s = s_new
            e = e_new
            
    return answer