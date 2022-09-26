'''
시각
: 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성하기
'''
N = int(input())

cnt = 0
# greedy 
for h in range(N+1):
    if '3' in str(h):
        cnt += 3600
    else:
        for m in range(60):
            if '3' in str(m):
                cnt += 60
            else: 
                for s in range(60):
                    if '3' in str(s):
                        cnt += 1
print(cnt)