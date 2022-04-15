import sys
N, k = map(int,sys.stdin.readline().split())
# K *미만* 소수만 구하면 됨! - 에라토스테네스의 체 : 직접 나누는 것보다 인덱스 배수로 제거하는게 훨씬 빠르다!
ls = [1]*k
for i in range(2, int(k**0.5)+1):
    if ls[i] == 1:
        for j in range(i*2,k,i):
            ls[j]=0
prime = [i for i in range(2,k) if ls[i] == 1]
good, bad = 1, 0
for n in prime:
    if N%n == 0:
        good, bad = 0, n
        break
print("GOOD" if good else f"BAD {bad}")