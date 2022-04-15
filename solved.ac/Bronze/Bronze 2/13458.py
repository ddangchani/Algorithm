import sys
n_room = int(sys.stdin.readline())
n_students = [int(i) for i in sys.stdin.readline().split()]
b, c = map(int, sys.stdin.readline().split())
n_supervisor = []
for i in range(n_room):
    if n_students[i] <= b:
        n_supervisor.append(1)
    else:
        extra = (n_students[i] - b)
        if extra % c == 0:
            n_supervisor.append(int(extra/c)+1)
        else:
            n_supervisor.append(int(extra/c)+2)

print(sum(n_supervisor))