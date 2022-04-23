# fibonacci function >> 재귀가 가장 느린 방식!

import sys
T = int(sys.stdin.readline())

zero = [1, 0, 1]  
one = [0, 1, 1] 

def fibonacci(N):
    length = len(zero)
    if N >= length:
        for i in range(length, N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[N],one[N]))
    
for t in range(T):
    N = int(sys.stdin.readline())
    fibonacci(N)