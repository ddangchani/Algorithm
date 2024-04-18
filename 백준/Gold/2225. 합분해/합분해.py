# 합분해

## add k integers in [0,N] so that the sum is N
## Find recurrence relation

N, K = map(int,input().split())

## DP > cumsum!

# Initialize > K=1
dp = [1] * (N+1) # N=0 then only one case 

def cumsum(ls):
    for i in range(1, len(ls)):
        ls[i] = (ls[i] + ls[i-1]) % int(1e9)
    return ls

for _ in range(K-1):
    dp = cumsum(dp)


print(dp[-1])