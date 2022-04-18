# 다리 놓기
# 서쪽 N, 동쪽 M >> M개 숫자 중 순서무관하게 N개를 뽑는 개수
import sys
T = int(sys.stdin.readline())
def factorial(n):
    return n * factorial(n-1) if n>1 else 1 # 재귀호출을 이용한 팩토리얼 구현

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(factorial(M)/(factorial(N)*factorial(M-N))))