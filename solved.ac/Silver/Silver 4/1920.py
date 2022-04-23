# 이진 탐색
import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def bin_search(target):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == target :
            return True
        
        elif N_list[mid] < target:
            left = mid + 1
        
        else:
            right = mid -1

for i in range(m):
    if bin_search(m_list[i]):
        print(1)
    else:
        print(0)