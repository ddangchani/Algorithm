N = int(input())
ls = list(map(int, input().split()))

ans = [ls.pop(0)]

def bisect(n, arr): # lower bound
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

for i in ls:
    # print(ans)
    if i > ans[-1]:
        ans.append(i)
    elif i == ans[-1]:
        continue
    else:
        idx = bisect(i, ans) + 1
        ans[idx] = i


print(len(ans))