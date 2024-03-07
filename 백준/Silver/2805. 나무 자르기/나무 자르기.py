# Check(x) : Total length when x >= M
# Binary Search : Check(left) = False, Check(right) = True


import sys

N, M = map(int, sys.stdin.readline().split())

ls = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(ls)

def total_parts(h):
    res = 0
    for l in ls:
        if l > h:
            res += l - h
    return res

while left <= right:
    mid = (left + right) // 2
    if total_parts(mid) >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right) # right > 최대값!