from math import ceil

def solution(n, stations, w):
    chunks = []
    now = 1
    for s in stations: # 오름차순 정렬
        if (s-w <= now) and (now <= s+w):
            now = s+w+1
            continue
        chunks.append([now, s-w-1])
        now = s+w+1
    
    # last chunk
    if now <= n:
        chunks.append([now, n])
        
    # count
    answer = 0
    for chunk in chunks:
        l = chunk[1] - chunk[0] + 1
        answer += int(ceil(l/(2 * w + 1)))

    return answer