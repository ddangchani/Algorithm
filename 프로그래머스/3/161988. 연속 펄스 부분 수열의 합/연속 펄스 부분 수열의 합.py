# Two pointer?

def solution(sequence): # len(seq) ~= 1e5 : No DP
    seq = [0]
    rev_seq = [0]
    for i,s in enumerate(sequence):
        if i % 2 == 0:
            seq.append(s)
            rev_seq.append(-s)
        else:
            seq.append(-s)
            rev_seq.append(s)

    n = len(seq)
    # cumsum
    for i in range(1, n):
        seq[i] += seq[i-1]
    
    for i in range(1, n):
        rev_seq[i] += rev_seq[i-1]
    
    
    # check max-min at i
    cur_min, ans = 1e9, 0
    for i,s in enumerate(seq):
        if s < cur_min:
            cur_min = s
        ans = max(ans, s - cur_min)
    
    cur_min = 1e9
    for i,s in enumerate(rev_seq):
        if s < cur_min:
            cur_min = s
        ans = max(ans, s - cur_min)
        
    return ans