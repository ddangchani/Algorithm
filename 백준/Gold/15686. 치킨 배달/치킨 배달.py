# Chicken
from itertools import combinations

N, M = map(int,input().split()) # M : number of chicken places
ls = []
houses = []
chickens = []
for r in range(N):
    to_append = list(map(int, input().split()))
    ls.append(to_append)
    for c, val in enumerate(to_append):
        if val == 1:
            houses.append([r,c])
        elif val == 2:
            chickens.append([r,c])

dist_mat = [[0] * len(houses) for _ in range(len(chickens))]

for r, v1 in enumerate(chickens):
    for c, v2 in enumerate(houses):
        dist_mat[r][c] = sum([abs(a-b) for a, b in zip(v1, v2)])

def chicken_dist(dist_mat):
    return sum(map(min, zip(*dist_mat)))

# Brute force : use combination
best = int(1e6)
for comb in combinations(range(len(chickens)), M):
    new_dist_mat = [dist_mat[r] for r in comb]
    new_dist = chicken_dist(new_dist_mat)
    if new_dist < best:
        best = new_dist

print(best)