from itertools import permutations
from math import ceil
def calculate(pick_idx, minerals):
    array = [[1,1,1],[5,1,1],[25,5,1]]
    pick_score = array[pick_idx]
    result = [a * b for a,b in zip(pick_score, minerals)]
    return sum(result)


# def solution(picks, minerals):
#     picks_ls = [0] * picks[0] + [1] * picks[1] + [2] * picks[2]
#     n_pickable = min(5 * sum(picks), len(minerals))
#     n_picks = ceil(n_pickable / 5) # 실제 사용해야할 곡괭이 수

#     answer = []

#     for pick_comb in list(set(permutations(picks_ls, n_picks))):
#         pick_comb = list(pick_comb)
#         cnt = 0
#         minerals_comb = minerals[:n_pickable]
#         pick = pick_comb.pop(0)
#         picked = 0

#         while minerals_comb:
#             cnt += calculate(pick, minerals_comb.pop(0))
#             picked += 1
#             if picked == 5 and minerals_comb:
#                 pick = pick_comb.pop(0)
#                 picked = 0

#         answer.append(cnt)

#     return min(answer) >> 시간초과 !

def solution(picks, minerals):
    picks_ls = [0] * picks[0] + [1] * picks[1] + [2] * picks[2]
    n_pickable = min(5 * sum(picks), len(minerals))
    minerals = minerals[:n_pickable]

    answer = []

    # 우선순위 정렬 ! (5개 단위)
    works = []
    for i, m in enumerate(minerals):
        div, mod = divmod(i, 5)
        if mod == 0:
            works.append([0,0,0])
        if m == "diamond":
            works[div][0] += 1
        elif m == "iron":
            works[div][1] += 1
        else:
            works[div][2] += 1

    works.sort(key=lambda x:[x[0],x[1],x[2]], reverse=True)
    # print(works)
    answer = 0
    for work in works:
        pick = picks_ls.pop(0)
        answer += calculate(pick, work)
    
    return answer

# picks = [1, 0, 1]
# minerals =  ["iron", "iron", "iron", "iron", "diamond", "diamond", "diamond"]
# print(solution(picks,minerals))