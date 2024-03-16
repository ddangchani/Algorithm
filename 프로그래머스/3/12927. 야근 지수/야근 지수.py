# IDEA : 최대값부터 줄여나가기 with bisect
# bisect for maximum value of work

def count_value(w, works):
    cnt = 0
    for i in works:
        cnt += max(0, i - w)
    return cnt

def bisect(v, works):
    left, right = 0, max(works)
    while left < right:
        mid = (left + right) // 2
        cnt = count_value(mid, works)
        if cnt > v:
            left = mid + 1
        else:
            right = mid
    
    return right

def solution(n, works):
    max_work = bisect(n, works)
    n_current = count_value(max_work, works)
    
    # Answer
    cnt = n - n_current
    print('cnt :', cnt, 'm_work : ', max_work)
    answer = 0
    for w in works:
        w = min(w, max_work)
        print(w)
        if cnt and w == max_work and w > 0:
            answer += (w-1) ** 2
            cnt -= 1
        else:
            answer += w ** 2
        # print(answer)
    
    return answer