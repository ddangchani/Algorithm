# 연산자 끼워넣기
import sys
import itertools
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
opers = list(map(int,sys.stdin.readline().split()))
oper_ls = []
for i,v in enumerate(opers):
    for _ in range(v):
        oper_ls.append(i)

def plus(now, new):
    return now+new
def minus(now, new):
    return now-new
def multiply(now, new):
    return now * new
def divide(now, new):
    if now < 0:
        return -((-now)//new)
    else:
        return now // new

oper_dict = {0:plus, 1:minus, 2:multiply, 3:divide}
res = []
for ls in set(itertools.permutations(oper_ls,len(oper_ls))):
    now = nums[0]
    for i, v in enumerate(ls):
        now = oper_dict[v](now, nums[i+1])
    res.append(now)
print(max(res))
print(min(res))