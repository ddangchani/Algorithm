import sys
T = int(sys.stdin.readline())
for t in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())
    d = ((x_1-x_2)**2 + (y_1-y_2)**2)**(0.5)
    d_1, d_2 = min([r_1, r_2]), max([r_1, r_2]) # 일반화
    if d == 0 : # 두 터렛 위치가 동일
        if d_1 != d_2: # 거리가 다름 > 불능
            print(0)
        else: # 거리 동일 > 원주
            print(-1)
    else:
        if d_2 > d_1 + d: # 삼각형 안만들어짐
            print(0)
        elif d > d_1 + d_2: # 삼각형 안만들어짐
            print(0)
        elif d_2 == d_1 + d: # 일직선상 1
            print(1)
        elif d == d_1 + d_2: # 일직선상 2
            print(1)
        else:
            print(2)