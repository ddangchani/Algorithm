from collections import deque

N, L, R = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]
M = len(ls[0])

# BFS approach
drc = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(r,c, arr, group_idx): # arr : group information, group_idx : current group information
    group = [[r,c]]
    arr[r][c] = group_idx
    q = deque([])
    q.append([r,c])
    while q:
        cr, cc = q.popleft()
        pop_cur = ls[cr][cc] # current population
        for dr, dc in drc:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            diff = abs(ls[nr][nc]-pop_cur)
            if arr[nr][nc] == 0: # Not grouped
                if diff >= L and diff <= R: # being grouped
                    arr[nr][nc] = group_idx
                    group.append([nr,nc])
                    q.append([nr,nc])

    return group

def move_pop(group_infos):
    for group in group_infos:
        popsum = sum([ls[r][c] for r,c in group])
        popeach = int(popsum / len(group))
        for r,c in group:
            ls[r][c] = popeach


# Count the day
day = 0
while True:
    arr = [[0] * M for _ in range(N)]
    group_infos = []
    group_idx = 1
    for n in range(N):
        for m in range(M):
            if arr[n][m] == 0:
                group_infos.append(bfs(n,m,arr,group_idx))
                group_idx += 1
    
    if len(group_infos) == N * M:
        break
    else:
        move_pop(group_infos)
        day += 1

print(day)


