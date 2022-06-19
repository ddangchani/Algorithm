import sys
N = int(sys.stdin.readline())
switch = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline())

for _ in range(n):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1:
        for i in range(num-1, N, num):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1                
                                                                                                    
    else:
        j = 0 # 대칭개수
        while j < min(num-1,N-num):
            j += 1
            if switch[num-1-j] == switch[num-1+j]:
                pass
            else:
                j -= 1
                break
        
        for o in range(num-j-1,num+j):
            if switch[o]:
                switch[o] = 0
            else:
                switch[o] = 1
                
# 출력
for b in range(N):
    print(switch[b], end = ' ')
    if (b+1) % 20 == 0:
        print()