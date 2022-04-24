# 에라토스테네스 체
import sys
m, n = map(int,sys.stdin.readline().split())
def prime(m,n):
    ls = [1] * (n+1) # N 이하까지 소수여부 체
    for i in range(2,int(n**0.5)+1):
        if ls[i] == 1:
            for j in range(i*2,n+1,i):
                ls[j] = 0

    for i,v in enumerate(ls):
        if i >= max(2,m) and v == 1:
            print(i)

prime(m,n)