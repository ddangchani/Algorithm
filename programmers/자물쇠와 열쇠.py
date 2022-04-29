def key_map(key, N, x, y):
    M = len(key)
    keymap = []
    for _ in range(y):
        keymap.append([0]* (N+2*M-2))
    for i in range(y, y+M):
        row = [0]*x + key[i-y] + [0]*(N+M-2-x)
        keymap.append(row)
    for _ in range(y+M, N+2*M-2):
        keymap.append([0]* (N+2*M-2))
    return keymap

def active_key(keymap, M, N): # lock map 위에 올려져있는 key value들 반환
    active = []
    for i in range(M-1, M+N-1):
         active.append(keymap[i][M-1:M+N-1])
    return active

def rotation_left(key):
    left = []
    for i in range(len(key)-1,-1,-1):
        left.append([j[i] for j in key])
    return left

def rotations(key):
    ls = []
    while len(ls)<4:
        key = rotation_left(key)
        ls.append(key)
    return ls

def solution(key, lock): # key M X M, lock N X N
    answer = False
    M, N = len(key), len(lock)
    for k in rotations(key):
        for x in range(N+M-1): # x,y좌표 : 0부터 N+M-2까지 취할 수 있음(그리드 개수는 N+2M-2)
            for y in range(N+M-1):
                keymap = key_map(k, N, x, y)
                key_active = active_key(keymap, M, N)
                result = [[x+y for x,y in zip(key_active[i],lock[i])] for i in range(N)]
                flatten = [y for x in result for y in x]
                if list(set(flatten)) == [1]:
                    answer = True
                    break
            if answer == True:
                break
        if answer == True:
            break

    return answer # True or False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


print(solution(key,lock))