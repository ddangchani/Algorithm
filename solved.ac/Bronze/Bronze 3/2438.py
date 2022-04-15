# 별찍기 1
import sys
N = int(sys.stdin.readline())

for i in range(1,N+1,1):
    print("".join(['*']*i))