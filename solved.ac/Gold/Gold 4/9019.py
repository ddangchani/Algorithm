import sys
from collections import deque

# 네 개의 함수 종류 구현 - 무조건 네자리 고정되어있음!!
def D(n):
    val = n * 2
    if val > 9999:
        return val%10000
    else:
        return val
def S(n):
    if n==0:
        return 9999
    else:
        return n-1
def L(n):
    return (n%1000)*10 + (n//1000)
    
def R(n):
    return (n%10)*1000 + (n//10)    
        
functions = {'D' : D, 'S' : S,  'L' : L, 'R' : R}

# 데이터 받기
N = int(sys.stdin.readline())
for _ in range(N):
    num, target = map(int, sys.stdin.readline().split())

# 그래프 탐색
    deq = deque()
    deq.append((num,'')) # 초기 값과 초기경로(빈 str) append
    visited = set() # 방문기록 저장
    visited.add(num)
    while deq:
        new, route = deq.popleft()
        if new == target: # 타겟에 도달한 경우 break
            print(route)
            break
        else:
            for f in ['D', 'S', 'L', 'R']:
                val = functions[f](new) # 새로 방문하는 값
                
                if (val not in visited) and (val != new): # 방문기록이 없고, 제자리 이동이 아닌경우
                    visited.add(val)
                    new_route = route + str(f)
                    deq.append((val,new_route))

import sys
from collections import deque
#sys.stdin = open("input.txt","r")

def oper_D(n): # D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
    res = n * 2
    if res > 9999:
        res %= 10000    
    return res

def oper_S(n): # S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
    res = n
    if res == 0: return 9999
    res -= 1
    return res


def oper_L(n): # 왼쪽으로 회전 : 1234 -> 2341    
    front = n % 1000
    back = n // 1000
    res = front*10 + back
    return res


def oper_R(n): # 오른쪽으로 회전 : 1234 -> 4123  
    front = n % 10
    back = n // 10
    res = front*1000 + back
    return res

def go(s, t):
    queue = deque()
    visited = set() # logn
    queue.append((s, "")) 
    visited.add(s)
    while queue:
        cur_num, oper = queue.popleft()
        if cur_num == t:
            print(oper)            
            return        
        tmp = oper_D(cur_num)        
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"D"))

        tmp = oper_S(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"S"))      

        tmp = oper_L(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"L"))

        tmp = oper_R(cur_num)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, oper+"R"))

for _ in range(int(input())):
    start, target = map(int, input().split()) 
    #print(start, target)  
    go(start, target)