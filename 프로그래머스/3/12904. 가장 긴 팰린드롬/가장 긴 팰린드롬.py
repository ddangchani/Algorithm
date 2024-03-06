# DP

def is_palindrome(word):
    return word == word[::-1]

def solution(s):
    length = len(s)
    
    memo = [[0] * length for _ in range(length)] 
    
    for i in range(length): 
        memo[i][i] = 1 # odd length palindrome
    for i in range(length-1):
        if s[i] == s[i+1]:
            memo[i][i+1] = 2
        
    for end in range(length):
        for start in range(end+1):
            if not memo[start][end]:
                if memo[start+1][end-1] and s[start] == s[end]:
                    memo[start][end] = memo[start+1][end-1] + 2
    
    answer = max([x for y in memo for x in y])
    
    return answer