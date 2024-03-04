import sys

T = int(sys.stdin.readline()) # number of test cases
n_ls = [int(sys.stdin.readline()) for _ in range(T)]

ans_ls = [0,1,2,4]

for n in n_ls:
    if len(ans_ls) > n:
        print(ans_ls[n])
    else:
        for i in range(len(ans_ls), n+1):
            to_append = ans_ls[-1] + ans_ls[-2] + ans_ls[-3]
            ans_ls.append(to_append)
        print(ans_ls[n])