# Dynamic Programming!

import sys
N = int(sys.stdin.readline())
n_calc = [0, 1, 1, 2, 3, 2] # minimum n_calc from 1 to N
if N >= len(n_calc) :
    for i in range(len(n_calc)+1, N+1):

        if i % 2 != 0 and i % 3 != 0: # 2,3모두로 안나눠짐
            n_calc.append(n_calc[i-2]+1)

        elif i % 3 == 0 and i % 2 != 0: # 3으로만 나눠짐
            x = n_calc[int(i/3)-1]+1
            y = n_calc[i-2]+1
            n_calc.append(min(x,y))

        elif i % 2 == 0 and i % 3 !=0: # 2로만 나눠짐
            a = n_calc[i-2]+1
            b = n_calc[int(i/2)-1]+1
            n_calc.append(min(a,b))

        else: # 2,3 둘다 나눠짐
            c = n_calc[int(i/2)-1]+1
            d = n_calc[int(i/3)-1]+1
            e = n_calc[i-2]+1
            n_calc.append(min(c,d,e))
            
print(n_calc[N-1])
