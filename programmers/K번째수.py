array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for command in commands:
    i, k, j = command
    ls = array[i-1:k]
    ls.sort()
    answer.append(ls[j-1])

print(answer)