# N개의 수 > 오름차순 정렬
import sys
input()
ls = sys.stdin.readlines()
res = [int(i) for i in ls]
res.sort()
for i in res:
    print(i)