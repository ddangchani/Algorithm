'''
큰 수의 법칙. 첫째 줄에 N, M, K 주어지고 둘째 줄에 N개의 자연수 공백으로 주어짐.
> 큰 수의 법칙 : 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙. 단 특정 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없음
'''
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

first, second = numbers[0:2]

n_second = M // (K+1)
n_first = M - n_second

print(first*n_first + second*n_second)