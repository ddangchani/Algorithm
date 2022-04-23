# Editor
# 핵심 > insert, remove > O(n) 대신 append, pop O(1)

from pickletools import string1
import sys
st1 = list(sys.stdin.readline().strip())
st2 = []
T = int(sys.stdin.readline())

for t in range(T):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if st1: st2.append(st1.pop())

    elif command[0] == 'D' :
        if st2: st1.append(st2.pop())

    elif command[0] == 'B':
        if st1: st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))