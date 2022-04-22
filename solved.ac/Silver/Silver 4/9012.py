# 핵심 : 스태킹 !

import sys
T = int(sys.stdin.readline())

for t in range(T):
    x = list(sys.stdin.readline().strip())
    ls = []
    earlystop = False
    for i, val in enumerate(x):
        if val == '(':
            ls.append(i)
        elif len(ls) == 0:
            earlystop = True
            break
        else:
            ls.pop()
    if earlystop:
        print('NO')
    else:
        print('YES' if len(ls) == 0 else "NO")