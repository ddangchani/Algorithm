N, M = map(int, input().split())

def backtrack(ls):
    if len(ls) == M:
        print(*ls)
        return
    for i in range(1, N+1):
        if ls and i >= ls[-1]:
            ls.append(i)
            backtrack(ls)
            ls.pop()
        elif not ls:
            ls.append(i)
            backtrack(ls)
            ls.pop()
    
   
backtrack([])