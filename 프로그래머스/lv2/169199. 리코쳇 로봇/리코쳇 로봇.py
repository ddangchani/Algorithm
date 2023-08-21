from collections import deque

# 최소거리 > BFS!

def move(current_coord, direction, board):
    y, x = current_coord
    if direction[0] == 0: # x축 이동일 때
        ls = board[y]
        while 0 <= x < len(ls):
            x += direction[1]
            if x < 0 or x >= len(ls):
                x -= direction[1]
                break
            if ls[x] == 'D':
                x -= direction[1]
                break
        return y, x
    
    else: # y축 이동일 때
        ls = [xs[x] for xs in board]
        while 0 <= y <= len(ls):
            y += direction[0]
            if y < 0 or y >= len(ls):
                y -= direction[0]
                break
            if ls[y] == 'D':
                y -= direction[0]
                break
        return y, x

def solution(board):
    width, height = len(board[0]), len(board)
    visited = [[0] * width for _ in range(height)]
    # index of Goal and Start
    for i,v in enumerate(board):
        if 'G' in v:
            goal_idx = [i, v.index('G')]
        if 'R' in v:
            start_idx = [i, v.index('R')]
    
    deq = deque([start_idx])
    visited[start_idx[0]][start_idx[1]] = 1
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    
    while deq:
        y, x = deq.popleft()
        current = visited[y][x]
        
        # append new coordinates
        for dirs in directions:
            new_y, new_x = move([y,x],dirs,board)
            if visited[new_y][new_x] == 0:
                deq.append([new_y, new_x])
                visited[new_y][new_x] = current + 1
            
    return visited[goal_idx[0]][goal_idx[1]] - 1