import sys
ls = [1,1,2,2,2,8]
have = sys.stdin.readline().split()
needs = []
for i in range(len(ls)):
    needs.append(str(int(ls[i])-int(have[i])))
print(' '.join(needs))