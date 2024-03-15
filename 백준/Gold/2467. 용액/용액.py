N = int(input())
ls = list(map(int, input().split()))
ls.sort() # sort!

# two pointer

def twopointer(ls=ls):
    left, right = 0, N-1
    best_abs = 2e9
    best_comb = [0,0]
    while left < right:
        # print(best_abs)
        current = ls[left] + ls[right]
        if best_abs > abs(current):
            best_comb = [left, right]
            best_abs = abs(current)
        if current == 0:
            break
        elif current > 0:
            right -= 1
        else:
            left += 1
    
    print(ls[best_comb[0]], ls[best_comb[1]])

twopointer(ls)

