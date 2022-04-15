# 메모리제한 8Mb >> 계수 정렬!
import sys
N = int(sys.stdin.readline())
array = [0] * 10001 # 0 부터 10000까지
for i in range(N):
    n = int(sys.stdin.readline())
    array[n] += 1
for i in range(10001):
    if array[i] !=0 :
        for j in range(array[i]):
            print(i)