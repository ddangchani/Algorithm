# 랜선 자르기
# 기존 K개 랜선으로 N개 이상 만들기 : 만들 수 있는 최대 랜선의 길이는?
import sys
K, N = map(int, sys.stdin.readline().split())
ls = []
for _ in range(K):
    ls.append(int(sys.stdin.readline()))

left = 1
right = max(ls)

while left <= right:
    mid = (left+right)// 2
    cnt = sum([i//mid for i in ls])
    if cnt < N:
        right = mid - 1
    else:
        left = mid + 1

print(right)