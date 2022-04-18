# 변수
import sys
L = int(sys.stdin.readline())
S = [int(s) for s in sys.stdin.readline().split()]
n = int(sys.stdin.readline())
if n in S:
    print(0)
else:
    S.append(n)
    S.sort()
    i = S.index(n)
    if i != 0:
        a = n - S[i-1] # 이전 수까지 간격
        b = S[i+1] - n # 다음 수까지 간격
        print(a*b -1)
    else: # n이 S의 최소보다 작은경우
        print(n*(S[1]-n)-1)