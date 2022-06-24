# 10844 : 쉬운 계단 수 >> 다이나믹 프로그래밍
import sys
N = int(sys.stdin.readline())
df = [[0]*10] # 초기 N=1 에서 실행할수록 데이터 저장
mod = 1000000000
# 1자리 계단수
for i in range(1,10):
    df[0][i] = 1

if N > len(df):
    for n in range(len(df)+1,N+1):
        new_col = [0]*10
        new_col[0] = df[-1][1]
        new_col[9] = df[-1][8]
        for j in range(1,9):
            new_col[j] = df[-1][j-1] + df[-1][j+1]
        df.append(new_col)
    num = sum(df[N-1])
else:
    num = sum(df[N-1])

print(num % mod)