# Lv2

n = 2
answer = []

def move(n, from_c, to_c):
    if n==1:
        return [[from_c, to_c]]
    else:
        new_c = [a for a in [1,2,3] if a not in [from_c,to_c]][0]
        return move(n-1, from_c, new_c) + [[from_c, to_c]] + move(n-1, new_c, to_c)

print(move(3,1,3))


