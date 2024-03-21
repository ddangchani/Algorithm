# IMOS!
from copy import deepcopy
def solution(board, skill):
    # access : board[row][col]
    # board 확장(padding 오른쪽, 아래 추가)
    nrow, ncol = len(board), len(board[0])
    checkboard = [[0] * (ncol+1) for _ in range(nrow+1)]
    
    # IMOS 전처리(직사각형 시작지점에 degree, 첫행/첫열 끝지점 + 1에 -degree)
    for s in skill:
        _type, r1, c1, r2, c2, degree = s
        degree = degree * (-1) if _type == 1 else degree
        checkboard[r1][c1] += degree
        checkboard[r1][c2+1] -= degree
        checkboard[r2+1][c1] -= degree
        checkboard[r2+1][c2+1] += degree
    
    # IMOS 후처리(누적합)
    ## 가로 누적합
    for r in range(nrow):
        for c in range(1, ncol):
            checkboard[r][c] += checkboard[r][c-1]
    ## 세로 누적합
    for c in range(ncol):
        for r in range(1, nrow):
            checkboard[r][c] += checkboard[r-1][c]

    # counting
    cnt = 0 
    for r in range(nrow):
        for c in range(ncol):
            if board[r][c] + checkboard[r][c] > 0:
                cnt += 1
    
    return cnt