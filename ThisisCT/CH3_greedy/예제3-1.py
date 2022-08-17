'''
문제. 거스름돈으로 500원, 100원, 50원, 10원짜리 동전이 주어짐. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하여라.
'''
N = int(input())
cnt = 0
coins = [500, 100, 50, 10]
for coin in coins:
    c, N = divmod(N, coin)
    cnt += c

print(cnt)