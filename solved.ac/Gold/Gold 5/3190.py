import sys
import copy

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = []
for _ in range(K):
    a,b = map(int, sys.stdin.readline().split()) # 각각 행(y), 열(x)
    apples.append([b-1,a-1]) # 사과 좌표

L = int(sys.stdin.readline())
dir = {} # 몇초 후 방향(L/D)
for _ in range(L):
    t, d = sys.stdin.readline().strip().split()
    dir[int(t)] = d

# 뱀 움직이는 것 클래스화

class snake:
    def __init__(self, N, apples, dir):
        self.stack = [[0,0]]
        self.info = [[0,1]] # vertical(수평이동중이면 0/수직이면 1), increasing(증가중이면 1/아니면 -1)
        self.N = N
        self.apples = apples
        self.dir = dir

    def turn_left(self): # 방향전환 > X초가 끝난 뒤에 발생
        new_info = []
        head_info = copy.deepcopy(self.info[0])
        if not head_info[0]:
            head_info[1] *= (-1)
        head_info[0] = int(not head_info[0])
        new_info.append(head_info)
        new_info.extend(self.info[1:])
        self.info = copy.deepcopy(new_info)
    
    def turn_right(self):
        new_info = []
        head_info = copy.deepcopy(self.info[0])
        if head_info[0]:
            head_info[1] *= (-1)
        head_info[0] = int(not head_info[0])
        new_info.append(head_info)
        new_info.extend(self.info[1:])
        self.info = copy.deepcopy(new_info)

    def move(self):
        new_stack = [] # move 결과 좌표값들
        new_info = [] # move 결과 좌표값들에 대한 운동정보
        temp_stack = copy.deepcopy(self.stack[-1])
        temp_info = copy.deepcopy(self.info[-1])

        self.stack[0][self.info[0][0]] += self.info[0][1] # head만 이동 > head만 collision check
        
        new_stack.append(self.stack[0])
        new_info.append(self.info[0])

        # Collision check > as ValueError
        new_x, new_y = new_stack[0]
        if new_x < 0 or new_x >= N:
            raise ValueError
        elif new_y < 0 or new_y >= N:
            raise ValueError
        
        if new_stack[0] in self.stack[1:]:
            raise ValueError

        # Error 없으면 이동

        if new_stack[0] in apples: # 사과 있는 경우
            apples.remove(new_stack[0]) # 사과 먹으면 반드시 먹은것으로 처리!
            for i in range(1,len(self.stack)):
                self.stack[i][self.info[i][0]] += self.info[i][1] # 각 점 이동
                new_stack.append(copy.deepcopy(self.stack[i])) # append
                new_info.append(copy.deepcopy(self.info[i-1])) # 새로 이동한 점은 이전에 위치한 점의 운동정보를 가짐
            new_stack.append(temp_stack)
            new_info.append(temp_info)

        else:
            for i in range(1,len(self.stack)):
                self.stack[i][self.info[i][0]] += self.info[i][1] # 각 점 이동
                new_stack.append(copy.deepcopy(self.stack[i])) # append
                new_info.append(copy.deepcopy(self.info[i-1])) # 새로 이동한 점은 이전에 위치한 점의 운동정보를 가짐

        self.stack = copy.deepcopy(new_stack)
        self.info = copy.deepcopy(new_info)


    def sketch(self):
        try:
            board = [[0]*N for _ in range(N)] # 빈 지도
            for coord in self.stack:
                board[coord[1]][coord[0]] = 1
            print(*board, sep='\n')
            print()
        except:
            pass

# 최종 계산
time = 0
s = snake(N,apples,dir)
try:
    while True:
        time += 1
        s.move()
        s.sketch() # Visualize movement
        if time in s.dir.keys():
            if dir[time] == 'L':
                s.turn_left()
            else:
                s.turn_right()

except ValueError:
    print(time)