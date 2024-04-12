def solution(a):
    if len(a) <= 2:
        return len(a)
    
    ## Check each side
    answer = 2 ## 양끝점 > 가능
    n = len(a)
    count = [0] * n
    left_min = a[0]
    for idx, val in enumerate(a[1:-1]):
        idx += 1
        ## If val > left_min : cnt += 1
        if val < left_min:
            count[idx] += 1
            # ## if the next right is smaller then count
            # if val > a[idx + 1]:
            #     count[idx] += 1          
        left_min = min(val, left_min)
        
        
    right_min = a[-1]
    for idx, val in enumerate(a[-2:0:-1]):
        idx = n-2-idx
        if val < right_min :
            count[idx] += 1
            # if val > a[idx-1] :
            #     count[idx] += 1
        
        if count[idx] >= 1: # count answer
            answer += 1
        right_min = min(val, right_min)
    
    return answer