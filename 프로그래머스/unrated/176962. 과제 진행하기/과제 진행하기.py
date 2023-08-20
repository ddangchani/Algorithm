from collections import deque

def get_time(time): # 시간을 string 대신 분으로 다루자!
    h, m = map(int, time.split(':')) 
    return 60 * h + m

def solution(plans):
    plans = [[a, get_time(b), int(c)] for a,b,c in plans]
    plans.sort(key=lambda x:x[1])
    currenttime = plans[0][1]
    keeps = deque([plans[0]])
    finished = []
    
    for plan in plans[1:]:
        next_time = plan[1]

        while keeps:
            keep = keeps.pop()

            if keep[1] > currenttime:
                currenttime = keep[1]
            
            after_keep = currenttime + keep[2]

            if after_keep <= next_time:
                currenttime += keep[2]
                finished.append(keep[0])
            else:
                currenttime = next_time
                keeps.append([keep[0], keep[1], after_keep - next_time])
                break

        keeps.append(plan)

    # plans 내부는 다 처리했을 때(keeps들만 처리하면 됨)
    while keeps:
        finished.append(keeps.pop()[0])
        
    return finished

