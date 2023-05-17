# 첫째 줄 수열에 속해 있는 수의 개수
# 둘째 줄부터 N개의 수 차례대로

N = int(input())
arr = [int(input()) for _ in range(N)]

arr = sorted(arr, reverse=True) # 내림차순

print(*arr)