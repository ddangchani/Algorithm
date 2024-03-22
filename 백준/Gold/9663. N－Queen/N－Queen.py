# N-queen

N = int(input())
cols = [False] * N
diag1 = [False] * (2*N-1) # / 방향 : row + col
diag2 = [False] * (2*N-1) # \ 방향 : (N-1) - (row - col)
cnt = 0

def back(row):
    global cnt
    if row == N: # N개 다 놓았을 때
        cnt += 1
        return

    for col in range(N):
        if (not cols[col]) and (not diag1[row+col]) and (not diag2[N-1-(row-col)]):
            cols[col] = True
            diag1[row+col] = True
            diag2[N-1-(row-col)] = True
            back(row+1)
            cols[col] = False
            diag1[row+col] = False
            diag2[N-1-(row-col)] = False

back(0)

print(cnt)