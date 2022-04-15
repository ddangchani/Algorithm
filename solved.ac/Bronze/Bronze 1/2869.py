import sys
a, b, v = map(int,sys.stdin.readline().split())
if (v-a)%(a-b)==0:
    print(int((v-a)/(a-b))+1)
else:
    print(int((v-a)/(a-b))+2)