import sys

N = int(sys.stdin.readline())
ls = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

def dfs(q, cnt): 
    # q : coordinate [x, y]
    ls[q[1]][q[0]] = 0
    for i in range(4):
        new_x, new_y = q[0] + dxs[i], q[1] + dys[i] # new coordinates (4 ways)
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
            continue
        if ls[new_y][new_x] == 0:
            continue
        cnt = dfs([new_x, new_y], cnt+1)

    return cnt


ans = []
for i in range(N):
    for j in range(N):
        if ls[j][i]:
            ans.append(dfs([i,j], 0) + 1)

ans.sort()
print(len(ans))
for a in ans:
    print(a)