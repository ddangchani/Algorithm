from heapq import heappop, heappush, heapify

N = int(input())
ls = [int(input()) for _ in range(N)]
heapify(ls)


# # Idea : 가장 작은 묶음이 많이 합쳐지도록!
# # 합친 후 정렬한 리스트에 넣기
# Note default heap : min_heap

cnt = 0
while len(ls) > 1:
    # print(cnt)
    first, second = heappop(ls), heappop(ls)
    new = first + second # 합친 묶음
    cnt += new
    heappush(ls, new)

print(cnt)