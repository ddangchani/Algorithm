result = [0,1,1,2]
def solution(n):
    if n < len(result):
        return result[n]
    else:
        for i in range(len(result),n+1):
            result.append((result[i-2] + result[i-1]) % 1234567)
        
        return result[n]