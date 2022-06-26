# Z모양
import sys
N, r, c = map(int, sys.stdin.readline().split())
coord = [] # 각 4분할에서 몇번째 위치(0,1,2,3) 인지 저장
lengths = []
r += 1 # 0행, 0열 시작이므로 1씩 증가
c += 1
length = 2**N # 초기 변의 길이
while True:
    length = length // 2
    if r <= length and c <= length:
        new_coord = 0
    elif r <= length and c > length:
        new_coord = 1
        c -= length
    elif r > length and c <= length:
        new_coord = 2
        r -= length
    else:
        new_coord = 3
        c -= length
        r -= length
    coord.append(new_coord)
    lengths.append(length)
    if length == 1:
        break
# answer print
ans = 0
for i in range(N):
    n = coord[i]
    l = lengths[i]
    ans += (l**2) * n
print(ans)
    
