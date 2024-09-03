# 경사로

N, L = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]

def transpose(ls):
    return list(map(list, zip(*ls)))

def check(ls):
    # check whether possible
    constructed = [0] * len(ls)
    c = 0
    while c < N-1:
        c_val = ls[c] # current elevation
        # diff c_val - next_val > 1: break
        n_val = ls[c+1]
        if abs(c_val-n_val) > 1:
            return False
        elif c_val-n_val == 1: # current higher
            # check c+1 ~ c+L same value
            if c+L >= N: # out of index
                return False
            else:
                _ls = ls[c+1:c+L+1]
                if len(set(_ls)) == 1 and sum(constructed[c+1:c+L+1]) == 0: # constructable
                    constructed[c+1:c+L+1] = [1]*L
                    c += L
                else:
                    return False
        
        elif c_val-n_val == -1: # curret lower
            # check c-L+1 ~ c
            if c-L+1 < 0: 
                return False
            else:
                _ls = ls[c-L+1:c+1]
                if len(set(_ls)) == 1 and sum(constructed[c-L+1:c+1]) == 0:
                    constructed[c-L+1:c+1] = [1]*L
                    c += 1
                else:
                    return False

        else: # same
            c += 1
    
    return True
        
cnt = 0

for sublist in ls:
    if check(sublist):
        cnt += 1
    
for sublist in transpose(ls):
    if check(sublist):
        cnt += 1

print(cnt)