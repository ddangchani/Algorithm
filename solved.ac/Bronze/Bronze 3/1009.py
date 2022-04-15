# 10으로 나눈 나머지 구하면 됨
import sys
sys.stdin.readline()
for l in sys.stdin.readlines():
    a,b = map(int,l.split())
    if b % 4 == 0:
        c=(((a%10)**4)%10)
    else:
        c=((a%10)**(b%4)%10)
    if c == 0:
        print(10) #0이 아니라 10 출력 !!!
    else:
        print(c)