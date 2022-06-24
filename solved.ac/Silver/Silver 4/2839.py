# 설탕 배달 > Dynamic Programming
import sys
N = int(sys.stdin.readline())
ls = [-1,-1,1,-1,1] # 1부터 5까지
if N > len(ls):
    for n in range(len(ls)+1,N+1):
        if ls[n-4]>0 and ls[n-6]>0:
            x = min(ls[n-4],ls[n-6])
            ls.append(x+1)
        elif ls[n-4] == -1 and ls[n-6] == -1:
            ls.append(-1)
        else:
            x = max(ls[n-4],ls[n-6])
            ls.append(x+1)

print(ls[N-1])