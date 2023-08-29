from collections import deque
from itertools import combinations

def check_count(word1, word2):
    if sum([a==b for a,b in zip(word1,word2)]) == length-1:
        return True
    
def solution(begin, target, words):
    global length
    length = len(begin)
    words = [begin] + words
    
    if target not in words:
        return 0
    else:
        target_idx = words.index(target)
    
    graph = [[] for _ in range(len(words))]
    for (i,word1),(j,word2) in combinations(enumerate(words),2):
        if check_count(word1, word2):
            graph[i].append(j)
            graph[j].append(i)
    
    deq = deque([0])
    visited = [0] * len(words)
    visited[0] = 1
    while deq:
        v = deq.popleft()
        for g in graph[v]:
            if not visited[g]:
                visited[g] = visited[v] + 1
                deq.append(g)
    
    answer = visited[target_idx]-1
    return answer