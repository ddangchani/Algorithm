N = int(input())
ls = list(map(int, input().split()))
ls.sort()

# Two pointer

left, right = 0, N-1
ans = int(3e9)
ans_pair = [0, 0]

while left < right:
    current = ls[left] + ls[right]
    # print(left, right)
    if abs(current) < ans:
        ans = abs(current)
        ans_pair = [left, right]
    if current > 0:
        right -= 1
    elif current < 0:
        left += 1
    else:
        break

print(ls[ans_pair[0]], ls[ans_pair[1]])