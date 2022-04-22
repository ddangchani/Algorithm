# 정수 저장 스택 구현
import sys
N = int(sys.stdin.readline())
ls = []
for i in range(N):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        ls.append(int(line[1]))
    elif line[0] == 'pop':
        if len(ls) != 0:
            print(ls.pop())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(ls))
    elif line[0] == 'empty':
        print(1 if len(ls) == 0 else 0)
    elif line[0] == 'top':
        print(ls[-1] if len(ls) != 0 else -1)


