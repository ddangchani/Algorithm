# Check(x) : Total number of wifi >= C
# Binary Search : Check(left) = False, Check(right) = True


import sys

N, C = map(int, sys.stdin.readline().split())
ls = [int(sys.stdin.readline()) for _ in range(N)]
ls.sort()

def count_num(dist):
    cnt = 1
    prev = ls[0]
    for i in range(1, N):
        if ls[i] - prev >= dist:
            prev = ls[i]
            cnt += 1
    return cnt

left = 1
right = ls[-1] - ls[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    if count_num(mid) >= C: # check(x)
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

# check(left) = False, check(right) = True
print(right)