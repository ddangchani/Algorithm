from collections import deque
from heapq import *
# DFS > k <= 2500이므로 불가!

def solution(n, m, x, y, r, c, k):
    # x, r : y axis, y, c : x axis
    visited = [[''] * m for _ in range(n)]
    dxdy = {'u' : [0,-1], 'd' : [0,1], 'l' : [-1,0], 'r' : [1,0]}
    dirs = ['u','d','l','r']
    dirs.sort() # alphabetically
    
    # BFS
    q = deque()
    q.append([y-1, x-1, '', 0]) # current x, y, path, path length
    while q:
        # print(q)
        cx, cy, path, pathlen = q.popleft()
        # break if
        if cx == c-1 and cy == r-1 and pathlen == k:
            return path
        if cx == c-1 and cy == r-1 and (k-pathlen) % 2 == 1:
            return 'impossible'
        
        for d in dirs:
            nx, ny = cx + dxdy[d][0] , cy + dxdy[d][1]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            # non-visitable
            if abs(c-1-nx) + abs(r-1-ny) > k-pathlen-1:
                continue
            q.append([nx,ny,path+d,pathlen+1])
            break
            
    return 'impossible'
    
    
