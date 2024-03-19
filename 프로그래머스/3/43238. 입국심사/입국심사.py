# Note : n ~= 1e9, time ~= 1e5 (possible?)

def calculate(t, times):
    ans = 0
    for i in times:
        ans += t // i
    return ans

def solution(n, times):
    # bisect for minimum time
    left, right = 0, int(1e18)
    # lower bound of 'calculate(t) >= n'
    while left < right:
        mid = (left + right) // 2
        if calculate(mid, times) < n:
            left = mid + 1
        else:
            right = mid
    
    return right