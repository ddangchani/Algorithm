# 숫자 카드 2 > 이진탐색 >> Dictionary 이용! > 개수는 저장, 숫자만 이진탐색
import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()

dic = {}
for n in n_list:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

def bin_count(target):
    left, right = 0, N-1
    while True:
        if left > right :
            return 0
        mid = (left+right) // 2

        if n_list[mid] == target:
            return dic.get(target)
        elif n_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

res = []
for m in range(M):
    res.append(bin_count(m_list[m]))
print(*res)

# bisect 구현 풀이 - 오류
# def count_left(value):
#     left = 0
#     right = N-1
#     while left <= right:
#         mid = (left+right) // 2
#         if n_list[mid] == value:
#             if mid == 0:
#                 return mid
#             elif n_list[mid-1] != value:
#                 return mid
#             else:
#                 right = mid-1
#         elif n_list[mid] < value:
#             left = mid+1
#         else:
#             right = mid-1

# def count_right(value):
#     left = 0
#     right = N-1
#     while left <= right:
#         mid = (left+right) // 2
#         if n_list[mid] == value:
#             if mid == N-1:
#                 return mid
#             elif n_list[mid+1] != value:
#                 return mid
#             else:
#                 left = mid + 1
#         elif n_list[mid] > value:
#             right = mid - 1
#         else:
#             left = mid + 1

# res = []
# for m in range(M):
#     target = m_list[m]
#     right = count_right(target)
#     if right:
#         res.append(right - count_left(target) + 1)
#     else:
#         res.append(0)
# print(*res)