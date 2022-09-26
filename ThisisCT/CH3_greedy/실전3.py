'''
숫자 카드 게임
첫째 줄에 숫자 카드들이 놓인 행의 개수, 열의 개수가 주어짐
둘째줄부터 카드의 숫자 주어짐
게임 룰 : 
'''
import sys

n, m = map(int, sys.stdin.readline().split())
ls_min = []
for _ in range(n):
    ls = list(map(int, sys.stdin.readline().split()))
    ls_min.append(min(ls))

print(max(ls_min))