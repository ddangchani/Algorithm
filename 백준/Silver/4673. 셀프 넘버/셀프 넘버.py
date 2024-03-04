check = [1] * 10001 # check whether self num or not

for i in range(1, 10001):
    if check[i]:
        print(i)
        n = i
        while True:
            next = sum(int(digit) for digit in str(n)) + n
            if next <= 10000:
                check[next] = 0
                n = next
            else:
                break
    else:
        pass