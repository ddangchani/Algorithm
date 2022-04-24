# 2048 game(Easy) > 포스팅하기
import sys
import itertools
import copy

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

# 네 방향으로의 개별 함수연산
def move_up(data):
    new_data = []
    for n in range(N): # 각 열에 대해
        blocks = list(map(list,zip(*data)))[n]
        new_blocks = []
        while 0 in blocks:
            blocks.remove(0)
        while True:
            if len(blocks) == 0:
                break  
            elif len(blocks) >= 2:
                if blocks[0] == blocks[1]:
                    new_blocks.append(blocks.pop(0)+blocks.pop(0))
                else:
                    new_blocks.append(blocks.pop(0))
            else:
                new_blocks.append(blocks.pop(0))

        new_blocks.extend([0]*(N-len(new_blocks)))
        new_data.append(new_blocks)
    ls = list(map(list,zip(*new_data)))
    return ls

def move_down(data):
    new_data = []
    for n in range(N): # 각 열에 대해
        blocks = list(map(list,zip(*data)))[n]
        new_blocks = []
        while 0 in blocks:
            blocks.remove(0)
        while True:
            if len(blocks) == 0:
                break  
            elif len(blocks) >= 2:
                if blocks[-1] == blocks[-2]:
                    new_blocks.append(blocks.pop(-1)+blocks.pop(-1))
                else:
                    new_blocks.append(blocks.pop(-1))
            else:
                new_blocks.append(blocks.pop(-1))

        new_blocks.extend([0]*(N-len(new_blocks)))
        new_data.append(reversed(new_blocks))
    ls = list(map(list,zip(*new_data)))
    return ls

def move_left(data):
    new_data = []
    for n in range(N): # 각 행에 대해
        blocks = data[n]
        new_blocks = []
        while 0 in blocks:
            blocks.remove(0)
        while True:
            if len(blocks) == 0:
                break  
            elif len(blocks) >= 2:
                if blocks[0] == blocks[1]:
                    new_blocks.append(blocks.pop(0)+blocks.pop(0))
                else:
                    new_blocks.append(blocks.pop(0))
            else:
                new_blocks.append(blocks.pop(0))

        new_blocks.extend([0]*(N-len(new_blocks)))
        new_data.append(new_blocks)
    return new_data

def move_right(data):
    new_data = []
    for n in range(N): # 각 행에 대해
        blocks = data[n]
        new_blocks = []
        while 0 in blocks:
            blocks.remove(0)
        while True:
            if len(blocks) == 0:
                break  
            elif len(blocks) >= 2:
                if blocks[-1] == blocks[-2]:
                    new_blocks.append(blocks.pop()+blocks.pop())
                else:
                    new_blocks.append(blocks.pop())
            else:
                new_blocks.append(blocks.pop())

        new_blocks.extend([0]*(N-len(new_blocks)))
        new_data.append(list(reversed(new_blocks)))
    return new_data

dict_move = {1 : move_up, 2 : move_down, 3 : move_left, 4 : move_right} # 딕셔너리에 각 함수 지정

def find_max(data, ls):
    for i in ls:
        data = dict_move[i](data)
    max_val = max(sum(data,[]))
    return max_val

max_vals = []
for ls in itertools.product([1,2,3,4],repeat=5): # itertools.product로 중복순열 구현
    data_ls = copy.deepcopy(data) # deepcopying > 이중리스트는 deepcopying 필요
    max_vals.append(find_max(data_ls, ls))

print(max(max_vals))
