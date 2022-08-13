import sys
ls = []
num = 0 # 자리수
n = int(sys.stdin.readline())
while n > len(ls):
    for i in range(int(10**num),int(10**(num+1))):
        if '666' in str(i):
            ls.append(i)
    num += 1
print(ls[n-1])