def solution(sticker):
    answer = 0
    l = len(sticker)
    # edge case (l = 1)
    if l == 1:
        return sticker[0]
    
    # 첫번째 스티커 떼는 경우 : 마지막 스티커 못뗌
    dp = [0] * (l-1)
    dp[0] = sticker[0]
    for i in range(1, l-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    # 두번째 스티커 떼는 경우 : 마지막 스티커 뗄 수 있음
    dp2 = [0] * (l-1)
    dp2[0] = sticker[1]
    for i in range(1, l-1):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i+1])

    return max(dp2[-1], dp[-1])