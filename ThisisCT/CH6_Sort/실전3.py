# 성적이 낮은 순서로 학생 출력하기
N = int(input())
arr = []
for _ in range(N):
    name, score = input().split(' ')
    arr.append([name, int(score)])

arr = sorted(arr, key=lambda item : item[1], )

print(*[i[0] for i in arr])