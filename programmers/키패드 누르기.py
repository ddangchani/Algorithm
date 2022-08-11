# 키패드 누르기
# 규칙 : 
from copy import deepcopy

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
answer = []
col_left = ['1','4','7','*']
col_right = ['3','6','9','#']
col_center = ['2','5','8','0']
cols = [col_left, col_center, col_right]
left_idx = [0,3]
right_idx = [2,3]
for _ in range(len(numbers)):
    num = str(numbers.pop(0))
    if num in col_left: #왼쪽열인경우
        answer.append('L')
        left_idx = [0, col_left.index(num)]
    elif num in col_right: # 오른쪽열인경우
        answer.append('R')
        right_idx = [2, col_right.index(num)]
    else:
        idx = [1, col_center.index(num)]
        dist_left = sum([abs(left_idx[i]-idx[i]) for i in range(2)])
        dist_right = sum([abs(right_idx[i]-idx[i]) for i in range(2)])
        if dist_left < dist_right:
            answer.append('L')
            left_idx = deepcopy(idx)
        elif dist_right < dist_left:
            answer.append('R')
            right_idx = deepcopy(idx)
        else:
            if hand == 'left':
                answer.append('L')
                left_idx = deepcopy(idx)
            else:
                answer.append('R')
                right_idx = deepcopy(idx)

print(answer)