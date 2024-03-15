from copy import deepcopy
N = int(input())
ls = list(map(int, input().split()))
dp = [[a] for a in ls]
    
for i in range(1,N):
    for j in range(i):
        if ls[j] < ls[i]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = deepcopy(dp[j] + [ls[i]])

dp.sort(key=lambda x:len(x))
print(len(dp[-1]))
print(*dp[-1])