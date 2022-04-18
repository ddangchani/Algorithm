import sys
N = int(sys.stdin.readline()) # 단어개수
length = [[] for _ in range(50)] # 핵심! [[]]*50 으로 하면 반복됨
for i in sys.stdin.readlines():
    i = i.strip()
    length[len(i)-1].append(i)
for j in range(50):
    if len(length[j]) > 0:
        words = sorted(list(set(length[j]))) # 중복제거
        print(*words, sep="\n")