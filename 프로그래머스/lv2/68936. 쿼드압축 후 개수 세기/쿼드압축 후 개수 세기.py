from itertools import chain

def divide(arr):
    n = len(arr)//2 # 새로운 배열의 가로 세로 크기
    new_arr = []
    new_arr.append([ls[:n] for ls in arr[:n]])
    new_arr.append([ls[n:] for ls in arr[:n]])
    new_arr.append([ls[:n] for ls in arr[n:]])
    new_arr.append([ls[n:] for ls in arr[n:]])
    return new_arr
    

def count(arr):
    cnt_0, cnt_1 = 0,0
    if len(set(chain.from_iterable(arr))) == 1:
        if arr[0][0] == 1:
            return [0,1]
        else:
            return [1,0]
    
    for sub_arr in divide(arr):
        
        chain_arr = list(chain.from_iterable(sub_arr))
        if set(chain_arr) == {0}:
            cnt_0 += 1
        elif set(chain_arr) == {1}:
            cnt_1 += 1
        else: # 한번 더 나눠야 될 때
            if len(chain_arr) == 4:
                cnt_1 += sum(chain_arr)
                cnt_0 += (4-sum(chain_arr))
            else:
                cnt_0, cnt_1 = [sum(x) for x in zip([cnt_0, cnt_1], count(sub_arr))]
    
    return cnt_0, cnt_1


def solution(arr):
    cnt_0, cnt_1 = count(arr)
    return [cnt_0, cnt_1]