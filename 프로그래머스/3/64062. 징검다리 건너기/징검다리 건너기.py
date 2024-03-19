# len 10^5 > Two pointer(sliding window)
## Find minimum of max value in each window
from heapq import *

def solution(stones, k):
    # k becomes window size
    q = [((-1) * val, idx) for idx, val in enumerate(stones[:k])]
    heapify(q)
    # initial max value of window
    cur = q[0][0] * (-1)
    
    for i in range(k, len(stones)):
        
        # move window
        heappush(q, (stones[i] * (-1), i))
        while q[0][1] <= i-k: # NOTE : if current max cannot be acquired from current window
            heappop(q)
        cur = min(cur, q[0][0] * (-1))
    
    return cur