# AC
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    if n>0:
        array = sys.stdin.readline().strip()[1:-1]
        array = [i for i in array.split(',')]
    else:
        array = sys.stdin.readline()
        array = []
    stacks = []
    inverse = 1
    for i in range(len(p)):
        if p[i] == 'R':
            inverse *= -1
        elif p[i] == 'D':
            stacks.append(inverse)
    left_idx = stacks.count(1)
    right_idx = len(array) - stacks.count(-1)
    # Result
    if left_idx > right_idx:
        print('error')
    else:
        array = array[left_idx:right_idx]
        if len(array) == 0:
            print('[]')

        elif inverse == 1:
            print('['+','.join(array)+']')
        else:
            print('['+','.join(list(reversed(array)))+']')