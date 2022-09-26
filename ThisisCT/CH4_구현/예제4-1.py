'''
상하좌우
'''
N = int(input())
commands = input().split()
x, y = 1, 1
for i in commands:
    if i == 'R' and x < N:
        x += 1
    elif i == 'L' and x > 1:
        x -= 1
    elif i == 'U' and y > 1:
        y -= 1
    elif i == 'D' and y < N:
        y += 1

print(*(y, x)) # 좌표 > 행과 열 변경