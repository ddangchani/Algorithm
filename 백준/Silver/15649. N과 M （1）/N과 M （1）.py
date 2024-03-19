N, M = map(int, input().split())
ans = [0] * M
isused = [False] * (N+1)

def back(n):
    if n == M: # 배열의 길이를 확인
        print(*ans)
        return 
    for i in range(1, N+1): # 1 ~ N 까지
        if not isused[i]: # O(1)로 변환가능
            isused[i] = True
            ans[n] = i 
            back(n+1)
            isused[i] = False

back(0)