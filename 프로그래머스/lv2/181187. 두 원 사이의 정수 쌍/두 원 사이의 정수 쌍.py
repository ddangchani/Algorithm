from math import floor, ceil, sqrt

def find_ys(x,r1,r2):
    y_max = floor(sqrt(r2**2 - x**2))
    if x > r1:
        y_min = 0
    else:
        y_min = ceil(sqrt(r1**2 - x**2))
    
    return y_max-y_min+1

def solution(r1, r2):
    cnt = 0
    for x in range(1, r2+1):
        cnt += find_ys(x,r1,r2)
    
    answer = 4 * cnt
    return answer