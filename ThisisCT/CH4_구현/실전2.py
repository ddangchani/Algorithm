xy = input()
x = ['a','b','c','d','e','f','g','h'].index(xy[0]) + 1
y = int(xy[1])

cases = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

cnt = 0
for c in cases:
    x_n = x + c[0]
    y_n = x + c[1]
    if (1<=x_n<=8) and (1<=y_n<=8) : 
        cnt +=1

print(cnt)
