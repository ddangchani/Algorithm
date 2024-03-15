# 14501 퇴사 > Dynamic 역순으로
import sys
# Data Load
N = int(sys.stdin.readline())
day = []
profit = []
for _ in range(N):
    d, p = map(int, sys.stdin.readline().split())
    day.append(d)
    profit.append(p)

dp = [0] # 역순 최대수익 : (N - i)번째 원소 - (i+1)째날에 대응
for i in reversed(range(N)): # 역순으로 탐색
    d, p = day[i], profit[i]
    if d > (N - i) : # 상담 불가능한 경우
        dp.append(dp[N-i-1])
    else:
        val = max(dp[N-i-1], dp[N-i-d] + p)
        dp.append(val)
        
print(dp.pop())