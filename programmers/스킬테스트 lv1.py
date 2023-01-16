# # 1. n이 제곱수인지 check
# def solution(n):
#     sqrt_n = int(n**0.5)
#     if sqrt_n**2 == n:
#         answer = (sqrt_n + 1)**2
#     else:
#         answer = -1

#     return answer

# 2. 비밀지도
def solution(n, arr1, arr2):
    sol1, sol2 = [], []
    for i in arr1:
        ls = []
        for _ in range(n):
            i, mod = divmod(i, 2)
            ls.append(mod)
        ls.reverse()
        sol1.append(ls)
    for i in arr2:
        ls = []
        for _ in range(n):
            i, mod = divmod(i, 2)
            ls.append(mod)
        ls.reverse()
        sol2.append(ls)

    answer = []

    for i in range(n):
        ls_i = ''
        for j in range(n):
            if sol1[i][j] == 0 and sol2[i][j] == 0:
                ls_i += ' '
            else:
                ls_i += '#'
        answer.append(ls_i)
    
    return answer