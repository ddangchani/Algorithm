from heapq import *

def solution(jobs):
    n_jobs = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    current = jobs[0][0]
    ans = 0
    q = []
    heappush(q, jobs.pop(0)[::-1])
    while q:
        # pop
        d, t = heappop(q)
        current += d
        ans += current - t
        # print(current)
        while jobs and jobs[0][0] <= current:
            heappush(q, jobs.pop(0)[::-1])
        # 대기시간(no queue)
        if jobs and not q:
            current = jobs[0][0]
            heappush(q, jobs.pop(0)[::-1])
            
    
    return ans // n_jobs