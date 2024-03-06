from heapq import heappop, heappush

def solution(genres, plays):
    cnt_plays = {i:0 for i in genres}
    cnt_idx = {i:[] for i in genres}
    
    for i in range(len(plays)):
        cnt_plays[genres[i]] += plays[i]
        cnt_idx[genres[i]].append(i)
        
    # sort cnt_plays
    cnt_plays = sorted(cnt_plays.items(), key=lambda x: -x[1])
    
    answer = []
    
    for g, _ in cnt_plays:
        
        plays_g = [plays[k] for k in cnt_idx[g]]
        idx_g = cnt_idx[g]
        
        if len(idx_g) == 1:
            answer.append(idx_g.pop())
        else:
            plays_g, idx_g = zip(*sorted(zip(plays_g, idx_g), key= lambda x: -x[0]))
            answer += idx_g[:2]
        
            
    return answer