N, K = map(int, input().split())
weights, values = [], []
pairs = [list(map(int, input().split())) for _ in range(N)]

res = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        wi, vi = pairs[n-1][0], pairs[n-1][1]
        if wi > k:
            res[n][k] = res[n-1][k]
        else:
            res[n][k] = max(res[n-1][k], res[n-1][k-wi] + vi) # Not contain vs contain without the last one

print(res[N][K])