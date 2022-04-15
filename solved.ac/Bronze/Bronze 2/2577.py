import sys
a,b,c = map(int,sys.stdin.readlines())
mul = list(str(a*b*c))
for n in range(0,10,1):
    cnt = mul.count(str(n))
    print(cnt)