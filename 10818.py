# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 내풀이
import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split(' ')))
nums.sort()
print = sys.stdout.write
print(f'{nums[0]} {nums[n-1]}')


# min, max 사용가능 for list
import sys
input() # 먼저 input으로 첫줄의 무의미한 N을 쳐냄
ls = [int(s) for s in sys.stdin.read().split]