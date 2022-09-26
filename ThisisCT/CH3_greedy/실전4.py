'''
1이 될 때까지
N input > 두 연산 중 하나 반복적으로 선택하여 수행
1. 1빼기
2. K로 나누기
'''
N, K = map(int,input().split())

cnt = 0

while N > 1:
    if N % K == 0:
        N = N // K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)