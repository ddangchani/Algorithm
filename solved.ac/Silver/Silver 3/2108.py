import sys
N = int(sys.stdin.readline())
data = []
ls = [0]*8001
for i in range(N):
    n = int(sys.stdin.readline())
    data.append(n)
    ls[n+4000] += 1

data.sort()
# 평균
print(round(sum(data)/N))
# 중앙값
print(data[N//2])
# 최빈값
mode_cnt = max(ls)
idx = ls.index(mode_cnt)
ls[idx] -= 1
if max(ls) != mode_cnt:
    print(idx - 4000)
else:
    idx = ls.index(mode_cnt)
    print(idx - 4000)
# 범위
print(max(data)-min(data))




# 원래코드 왜 안되나 검토! > 최빈값 문제없음

# ls = [0]*8001
# sum = 0

# for i in range(N):
#     n = int(sys.stdin.readline())
#     ls[n+4000] += 1
#     sum += n
# # 산술평균
# print(round(sum/N))

# # 중앙값
# cnt = 0
# for i in range(8002):
#     cnt += ls[i]
#     if cnt > N//2:
#         print(i-4000)
#         break
#     else:
#         pass

# # 범위
# range = len(''.join(list(map(str,ls))).strip('0'))-1

# print(range)