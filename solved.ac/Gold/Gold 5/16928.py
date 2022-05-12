# 뱀과 사다리 게임
from collections import deque
import sys
N, M = map(int,sys.stdin.readline().split())
ladder = {}
snake = {}
for _ in range(N):
    key, val = map(int,sys.stdin.readline().split())
    ladder[key] = val
for _ in range(M):
    key, val = map(int,sys.stdin.readline().split())
    snake[key] = val

deq = deque([1])
ls = [1,2,3,4,5,6]
array = [0]*101
while deq:
    x = deq.popleft()
    for dx in ls:
        nx = x + dx
        if (0<nx<=100) and (array[nx] == 0):
            if nx in snake.keys():
                nx = snake[nx] # 이동하는 개념으로!

            if nx in ladder.keys():
                nx = ladder[nx] # 이동하는 개념으로!

            if array[nx] == 0:
                deq.append(nx)
                array[nx] = array[x] + 1

print(array[100])