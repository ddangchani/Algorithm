def _reverse(w):
    ans = ''
    for c in w:
        if c == '(':
            ans += ')'
        else:
            ans += '('
    return ans

def separate(w):
    cnt_left = 0
    perfect = True
    l = ''
    for c in w:
        l += c
        if c == '(':
            cnt_left += 1
        else:
            cnt_left -= 1
            
        if cnt_left < 0: # check perfect
            perfect = False
        if cnt_left == 0:
            break
    return l, w[len(l):], perfect
    
def dfs(w):
    if w == '':
        return ''
    u, v, u_perfect = separate(w)
    if u_perfect:
        return u + dfs(v)
    else:
        return '(' + dfs(v) + ')' + _reverse(u[1:-1])
    
def solution(p):
    return dfs(p)
    