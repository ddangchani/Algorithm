N = int(input())
ls = list(map(int, input().split()))

# sort
ls.sort()

def twopointer_find(v, arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == v:
            return True
        elif arr[left] + arr[right] > v:
            right -= 1
        else:
            left += 1
    return False

ans = []
for i in range(N):
    search = ls[:i] + ls[i+1:]
    if twopointer_find(ls[i], search):
        ans.append(ls[i])

print(len(ans))