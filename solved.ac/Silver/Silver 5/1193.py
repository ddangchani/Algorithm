# 분수 찾기

X = int(input())

n = int((2*X)**0.5) # 2X = n(n+1) + 2k

if 2*X-n**2-n <= 0:
    n -= 1

k = (2*X - n * (n+1)) // 2

if n % 2 == 0:
    print(f'{n+2-k}/{k}')

else:
    print(f'{k}/{n+2-k}')