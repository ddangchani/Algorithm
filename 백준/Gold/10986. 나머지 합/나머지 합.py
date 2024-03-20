import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
ls = [x % M for x in ls]

# two pointer

ans = 0
l = len(ls)
cumsum = [0]

for idx, val in enumerate(ls): # O(N)
    cumsum.append((val + cumsum[-1]) % M)

ans_dict = defaultdict(int)
for i in cumsum: # O(M)
    ans_dict[i] += 1

for k, v in ans_dict.items(): # O(M)
    if v > 1:
        ans += v * (v - 1) // 2

print(ans)
