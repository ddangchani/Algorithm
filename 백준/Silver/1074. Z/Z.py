# Z shape

# Divide and conquer?

import sys
N, r, c = map(int, sys.stdin.readline().split())

sample = [[0,1],[2,3]]

def conquer(N, r, c):
    if N == 1:
        return sample[r][c]
    else:
        return conquer(N-1, r%(2**(N-1)), c%(2**(N-1))) + int(2 ** (2*N-2)) * sample[r//(2**(N-1))][c//(2**(N-1))] # starting number of each quadrat

print(conquer(N,r,c))