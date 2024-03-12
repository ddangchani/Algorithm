def query_lower(q):
    lq = len(q)
    mask_idx = q.index('?')
    return q[:mask_idx] + 'a' * (lq - mask_idx)

def query_upper(q):
    lq = len(q)
    mask_idx = q.index('?')
    return q[:mask_idx] + 'z' * (lq - mask_idx)
    

def bisect(words, query):
    lq = len(query)
    lo, hi = 0, len(words)
    while lo < hi:
        mid = (lo + hi) // 2
        if len(words[mid]) < lq:
            lo = mid + 1
        elif len(words[mid]) > lq:
            hi = mid
        else:
            if words[mid] < query:
                lo = mid + 1
            else:
                hi = mid
    return hi
        

def solution(words, queries):
    words.sort(key=lambda x: (len(x), x)) # 정렬
    r_words = [w[::-1] for w in words]
    r_words.sort(key=lambda x: (len(x), x))
    
    answer = []
    for q in queries:
        if q[0] == '?' : # prefix
            q = q[::-1]
            up = bisect(r_words, query_upper(q))
            bot = bisect(r_words, query_lower(q))
        else:
            up = bisect(words, query_upper(q))
            bot = bisect(words, query_lower(q))
    
        answer.append(up - bot)
    
    return answer