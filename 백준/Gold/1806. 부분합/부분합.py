import sys

N, S = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

# two pointer

left, right = 0,0
cur = ls[0]
ans = int(1e6)
l = len(ls)

while left <= right:
    # print(left, right)
    if cur < S:
        if right < l-1:
            right += 1
            cur += ls[right]
        else:
            cur -= ls[left]
            left += 1
    else:
        ans = min(ans, right-left+1)
        cur -= ls[left]
        left += 1

if ans == int(1e6):
    ans = 0

print(ans)