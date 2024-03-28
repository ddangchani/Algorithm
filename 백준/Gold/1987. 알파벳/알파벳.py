# Alphabet >> DFS + backtrack
import sys
sys.setrecursionlimit(10**5)

R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
alphabets = set()
alphabets.add(arr[0][0])
ans = 1
dr, dc = [1,-1,0,0], [0,0,1,-1]

def backtrack(r, c, current):
    global ans
    ans = max(ans, current)
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<=nr<R and 0<=nc<C and not arr[nr][nc] in alphabets:
            alphabets.add(arr[nr][nc])
            backtrack(nr, nc, current+1)
            alphabets.remove(arr[nr][nc])
        
backtrack(0,0,1)

print(ans)