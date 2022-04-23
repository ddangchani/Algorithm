# 랜선 자르기
# 기존 K개 랜선으로 N개 이상 만들기 : 만들 수 있는 최대 랜선의 길이는?
import sys
K, N = map(int, sys.stdin.readline().split())
ls = [int(i) for i in sys.stdin.readlines()]