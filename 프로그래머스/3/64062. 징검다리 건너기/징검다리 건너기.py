# len 10^5 > Two pointer(sliding window)

def solution(stones, k):
    answer = max(stones[:k])
    # window size k
    for i in range(len(stones)-k):
        answer = min(answer, max(stones[i:i+k]))
    
    return answer