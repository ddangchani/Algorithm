from collections import deque

directions = [[0,-1],[0,1],[1,0],[-1,0]]
    

def solution(maps):
    width, height = len(maps[0]), len(maps)
    visited = [[0] * width for _ in range(height)]
    visited[0][0] = 1
    deq = deque([[0,0]])
    while deq:
        y, x = deq.popleft()
        for direction in directions:
            y_new, x_new = y + direction[0], x + direction[1]
            if (0 <= y_new < height) and (0 <= x_new < width) and (maps[y_new][x_new] == 1):
                if visited[y_new][x_new] == 0:
                    deq.append([y_new,x_new])
                    visited[y_new][x_new] = visited[y][x] + 1
        
    answer = visited[height-1][width-1]
    if answer == 0:
        return -1
    else:
        return answer