def solution(scores):
    wanho = scores[0]
    scores = scores[1:]
    wanho_total = sum(wanho)
    # 첫 번째 원소를 기준으로 내림차순 탐색하므로, 두번째 원소를 오름차순으로 탐색하며 최댓값을 임계치로 설정
    scores.sort(key=lambda x: (-x[0], x[1]))
    cnt = 0 # 완호보다 석차가 높은 사람 수
    threshold = 0 
    for a, b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1
        if b >= threshold:
            threshold = b

            if a + b > wanho_total:
                cnt += 1
    
    return cnt+1
    
    