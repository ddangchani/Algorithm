# n = 1e6, cmd = 1e5
def solution(n, k, cmd):
    cur = k # 현재 커서 위치
    deleted = [] # 삭제된 행 stack
    # D, U 명령어
    down = {i : i+1 for i in range(n)}
    up = {i : i-1 for i in range(n)}
    down[-1] = 0
    up[n] = n-1 # 마지막 행 선택
    
    
    for c in cmd:
        c = c.split(' ')
        if c[0] == 'D':
            for _ in range(int(c[1])):
                cur = down[cur]
        elif c[0] == 'U':
            for _ in range(int(c[1])):
                cur = up[cur]
        elif c[0] == 'C': # delete 
            d = down.pop(cur)
            u = up.pop(cur)
            down[u] = d
            up[d] = u
            deleted.append([cur, d, u])
            if d == n:
                cur = u
            else:
                cur = d
        else: # undo
            c, d, u = deleted.pop()
            down[c] = d
            up[c] = u
            down[u] = c
            up[d] = c
    
    answer = ''
    for i in range(n):
        if i in down:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer