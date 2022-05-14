# 스타트와 링크
import sys
from itertools import combinations, permutations
N = int(sys.stdin.readline())
array = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
comb = list(combinations(range(N),N//2))
n_comb = len(comb) # 전체 조합 개수
diff = []
for i in range(n_comb//2): # 전체 조합 중 절반 > 나머지 절반은 자동으로 구해지므로
    j = n_comb - 1 - i # 대응되는 상대팀 조합
    start = 0
    link = 0
    for a,b in permutations(comb[i],2):
        start += array[a][b]
    for c,d in permutations(comb[j],2):
        link += array[c][d]
    diff.append(abs(start-link))

print(min(diff))
    