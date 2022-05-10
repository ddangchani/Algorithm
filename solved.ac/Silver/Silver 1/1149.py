# RGB거리
import sys
N = int(sys.stdin.readline())
cost = [list(map(int,sys.stdin.readline().split()))] # 각 지점에서 R,G,B를 선택했을 때 최소 cost
for i in range(1,N):
    r,g,b = map(int,sys.stdin.readline().split())
    cost_i = [0,0,0]
    cost_i[0] = r+min(cost[i-1][1],cost[i-1][2])
    cost_i[1] = g+min(cost[i-1][0],cost[i-1][2])
    cost_i[2] = b+min(cost[i-1][0],cost[i-1][1])
    cost.append(cost_i)
print(min(cost.pop()))