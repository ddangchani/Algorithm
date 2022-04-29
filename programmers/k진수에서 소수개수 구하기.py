def to_k(n,k):
    res = ''
    while n>0:
        n, mod = divmod(n,k)
        res += str(mod)
    return res[::-1]

def check_prime(num):
    is_prime = 1
    for i in range(2,int(num**0.5)+1,1):
        if num % i == 0:
            is_prime = 0
            break
    return bool(is_prime)

def solution(n, k):
    ls = to_k(n, k).split('0')
    ls = list(filter(None, ls)) # remove None strings
    ls = list(map(int, ls))
    answer = 0
    for num in ls:
        if num > 1 and check_prime(num):
            answer += 1
    return answer