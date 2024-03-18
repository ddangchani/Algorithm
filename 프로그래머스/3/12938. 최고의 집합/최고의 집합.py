def solution(n, s):
    div = s // n
    if div <= 0:
        return [-1]
    else:
        div, mod = divmod(s, n)
        ans = [div] * (n - mod) +  [div + 1] * mod
        return ans