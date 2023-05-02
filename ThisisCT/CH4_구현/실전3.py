# 첫째줄 세로크기 N, 가로크기 M
N, M = map(int, input().split())

# 둘째줄 좌표 및 방향
a, b, d = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(N)]

# Rule
# 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 갈곳 설정

ds = [0,1,2,3]

da = [-1,0,1,0]
db = [0,1,0,-1]

visited = [[a,b]]

while True:
    cnt = 0
    for i in range(d-1,d-5,-1):
        cnt += 1
        na, nb = a + da[ds[i]], b + db[ds[i]]
        if ([na,nb] not in visited) and (ls[na][nb] == 0) and (0<=na<=N-1) and (0<=nb<=M-1):
            a, b = na, nb
            d = ds[i]
            visited.append([a,b])
            break
    
    if cnt >= 4:
        na, nb = a - da[ds[i]-1], b - db[ds[i]-1] # 기존 방향에서 뒤로
        if ls[na][nb] == 1:
            break
        else:
            a = na, b = nb, d = ds[i]-1

print(visited)

