# Queue
from collections import deque

def solution(A, B):
    answer = -1
    A.sort(reverse=True)
    B.sort(reverse=True)
    A = deque(A)
    B = deque(B)
    
    cnt = 0
    while A and B:
        a = A.popleft()
        b = B.popleft()
        if b > a:
            cnt += 1
        else:
            B.appendleft(b)
    
    return cnt