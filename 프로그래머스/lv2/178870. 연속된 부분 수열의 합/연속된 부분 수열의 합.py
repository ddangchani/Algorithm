def twopointer(sequence, k):
    answers = []
    cumsum = 0
    e = 0 # right pointer

    for s in range(len(sequence)): # left pointer
        while e < len(sequence) and cumsum < k:
            cumsum += sequence[e]
            e += 1
        
        if cumsum == k:
            answers.append([s,e-1])

        cumsum -= sequence[s] # overflow
        
    answers.sort(key=lambda x: [x[1]-x[0],x[0]])
    return answers[0]

def solution(sequence, k):
    if k in sequence:
        answer = [sequence.index(k),sequence.index(k)]
    else:
        answer = twopointer(sequence, k)
    return answer