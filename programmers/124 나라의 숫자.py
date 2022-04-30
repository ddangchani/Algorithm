def solution(n):
    res = []
    a = 0
    cnt = 1 # 자리수 카운트
    while n-a > 3**cnt:
        a += 3**cnt
        cnt += 1 
    n -= a+1
    while cnt:
        n, k = divmod(n,3)
        res.append(k)
        cnt -= 1
    res = list(reversed(res))
    for i,v in enumerate(res):
        if v == 2:
            res[i] = 4
        elif v == 1:
            res[i] = 2
        elif v == 0:
            res[i] = 1
    ls = [str(i) for i in res]

    return int(''.join(ls))