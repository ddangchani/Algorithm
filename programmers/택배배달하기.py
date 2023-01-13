# 택배 배달과 수거하기 (Lv.2)
# 2023 KAKAO Blind Recruitment

cap = int(input())
n = int(input())
deliveries = list(map(int, input().split()))
pickups = list(map(int, input().split()))

moved = 0 # 이동한 거리
max_dist = 0

delivery, pickup = 0, 0

while deliveries:
    while True:
        d = deliveries.pop()
        p = pickups.pop()
        if d > 0 or p > 0:
            max_dist = max(len(deliveries) + 1, max_dist) # 최대 이동거리
        delivery += d
        pickup += p

        if (delivery > cap) or (pickup > cap): # 용량 초과시 break
            break
        if len(deliveries) == 0:
            break

    delivery -= cap
    pickup -= cap
    if delivery > 0 or pickup > 0:
        deliveries.append(delivery)
        pickups.append(pickup)

    moved += max_dist * 2
    max_dist = 0
    delivery, pickup = 0, 0
    print(deliveries)

print(moved)










# def solution(cap, n, deliveries, pickups):
#     answer = -1
#     return answer