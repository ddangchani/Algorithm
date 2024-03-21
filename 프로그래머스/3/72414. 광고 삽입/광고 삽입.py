# 누적합(IMOS) : logs ~= 1e5
def timetoint(t):
    h,m,s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def inttotime(t):
    h, ms = divmod(t, 3600)
    m, s = divmod(ms, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)

def solution(play_time, adv_time, logs):
    l = timetoint(play_time)
    imos = [0] * (l+1) # imos check array
    for log in logs: # O(1e5)
        start, end = map(timetoint, log.split('-'))
        imos[start] += 1
        imos[end] -= 1
        
    # prefix sum (O(1e4)) : i 시점에 시청 중인 사람 수
    for i in range(1, l+1):
        imos[i] += imos[i-1]
    
    # prefix sum : i시점까지 시청한 전체 시청 시간
    for i in range(1, l+1):
        imos[i] += imos[i-1]
    
    # 부분합 : i - adv_time 시점부터 i 시점까지의 부분 누적 시청 시간
    adv = timetoint(adv_time)
    ans = imos[:adv].copy()
    for i in range(adv, l+1):
        ans.append(imos[i] - imos[i-adv])
        
    # result
    ans_i = max(ans) # O(l)
    # print(ans_i)
    
    answer = max(0,ans.index(ans_i) - adv + 1)
        
    
    return inttotime(answer)