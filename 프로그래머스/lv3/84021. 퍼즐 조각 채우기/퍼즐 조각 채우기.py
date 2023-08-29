from copy import deepcopy

global directions
directions = [[-1,0],[1,0],[0,1],[0,-1]]

def rotate(block):
    global size
    new_block = []
    for b in block:
        new_block.append([b[1], size-1-b[0]])
    return new_block

def move(hole, block):
    hole.sort()
    block.sort()
    mv_hole = [hole[0][0]-block[0][0], hole[0][1]-block[0][1]]
    for h in hole:
        if [h[0]-mv_hole[0], h[1]-mv_hole[1]] not in block:
            return False
    return True

def equal(hole, block):
    for _ in range(4):
        if move(hole, block):
            return True
        block = rotate(block)
    return False

def dfs(v, visited, n_block):
    visited[v[0]][v[1]] = n_block
    hole.append(v)
    block.append(v)
    for d in directions:
        next_v = [v[0]+d[0], v[1]+d[1]]
        if 0<=next_v[0]<size and 0<=next_v[1]<size:
            if visited[next_v[0]][next_v[1]] == 0:
                dfs(next_v, visited, n_block)
                
    
def solution(game_board, table):
    global size, visited, holes, blocks, hole, block
    size = len(game_board)
    visited = deepcopy(game_board)
    answer = 0
    n_block = 2
    holes, blocks = [], []
    hole = []
    block = []
    for y in range(size):
        for x in range(size):
            if visited[y][x] == 0:
                dfs([y,x], visited, n_block)
                n_block += 1
                holes.append(hole)
                hole = []
                block = []

    n_block = 2
    visited = []
    for y in range(size):
        visited.append(list(map(lambda x: 0 if x==1 else 1, table[y])))

    block = []
    for y in range(size):
        for x in range(size):
            if visited[y][x] == 0:
                dfs([y,x], visited, n_block)
                n_block += 1
                blocks.append(block)
                block = []
                hole = []
    
    holes.sort(key=lambda x: len(x), reverse=True)
    blocks.sort(key=lambda x: len(x), reverse=True)
    # print([len(x) for x in holes])

    used = [False for _ in range(len(blocks))]

    for hole in holes:
        for i, block in enumerate(blocks):
            if not used[i] and len(hole) == len(block):
                if equal(hole, block):
                    used[i] = True
                    answer += len(hole)
                    break
                    

    return answer