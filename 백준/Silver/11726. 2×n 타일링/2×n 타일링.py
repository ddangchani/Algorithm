import sys

N = int(sys.stdin.readline()) # n (column size)

cnt = [1,2]

if N <= 2:
    print(cnt[N-1])
else:
    for i in range(3, N+1):
        cnt.append((cnt[-2] + cnt[-1]) % 10007) # Modular
    print(cnt[-1])