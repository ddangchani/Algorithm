import sys

N = int(sys.stdin.readline()) # number of glasses

costs = [list(map(int, sys.stdin.readline().split()))]

for i in range(1, N):
    r, g, b = map(int, sys.stdin.readline().split())
    cost_r = min(costs[-1][1], costs[-1][2]) + r
    cost_g = min(costs[-1][0], costs[-1][2]) + g
    cost_b = min(costs[-1][0], costs[-1][1]) + b

    costs.append([cost_r, cost_g, cost_b])

print(min(costs[-1]))