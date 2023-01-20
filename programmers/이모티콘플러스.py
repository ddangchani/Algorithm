from itertools import product

def discount(emoticons, rate_discount) :  # 각 이모티콘의 할인가 계산
    discounted_price = []
    for i in range(len(emoticons)) : 
        discounted_price.append(int(emoticons[i] * (100 - rate_discount[i]) / 100))
    return discounted_price

def calculate(users, emoticons, rate_discount) : # 각 할인율별 가입자 및 판매결과계산
    sales = 0
    subscribers = 0
    discounted_price = discount(emoticons, rate_discount)
    for ls in users:
        per, margin = ls
        idx_bought = [r for r, v in enumerate(rate_discount) if v >= per]
        boughts = sum([discounted_price[i] for i in idx_bought])
        if boughts >= margin :
            subscribers += 1
        else:
            sales += boughts
    
    return [subscribers, sales]


def solution(users, emoticons):
    answer = [0, 0]

    for rate_discount in product([10,20,30,40], repeat = len(emoticons)) : 
        answer_i = calculate(users, emoticons, rate_discount)
        answer = max(answer, answer_i)

    return answer