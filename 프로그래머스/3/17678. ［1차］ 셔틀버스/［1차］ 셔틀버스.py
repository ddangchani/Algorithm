from heapq import *

def timetoint(timestr):
    h,m = map(int, timestr.split(':'))
    return 60 * h + m
    
first_bus = 9*60 # 09:00

def inttotime(timeint):
    div, mod = divmod(timeint, 60)
    return str(div).zfill(2)+':'+str(mod).zfill(2)
    
def solution(n, t, m, timetable):
    q = []
    for i in timetable:
        heappush(q, timetoint(i))
        
    _time = first_bus # 현재 시각
    for _ in range(n-1): # 마지막 이전 버스까지 다 태우기 (O(n))
        cnt = 0
        while q[0] <= _time and cnt < m:
            heappop(q)
            cnt += 1
        _time += t
        
    # 마지막 버스 : _time에 출발
    cnt = m # 마지막 버스에 남은 자리
    mintime = q[0] # 마지막 버스에 처음 탑승하는 사람
    # case 0 : 남은 사람들이 탑승 불가
    if mintime > _time:
        return inttotime(_time)
    
    # 탑승 시작
    while cnt > 1 and q:
        heappop(q)
        cnt -= 1
    # case 1 : 자리가 있을 때
    if not q: # 사람들이 다 탑승
        print('case1')
        return inttotime(_time)
    # case 2 : 자리가 없을 때
    else:
        if q[0] == mintime:
            return inttotime(mintime-1)
        else:
            return inttotime(q[0]-1)
    