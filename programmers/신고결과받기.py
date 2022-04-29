def solution(id_list, report, k):
    report = list(set(report)) # 중복신고 제거
    rep = [i.split(' ') for i in report]
    array = [[0]*len(id_list) for _ in range(len(id_list))]
    for i in range(len(rep)):
        sent = id_list.index(rep[i][0])
        received = id_list.index(rep[i][1])
        array[sent][received] += 1
    
    banned = [0] * len(id_list)
    array_T = list(map(list,zip(*array)))
    for i in range(len(id_list)):
        if sum(array_T[i]) >= k:
            banned[i] = 1
    
    answer = []
    for i in range(len(id_list)):
        cnt = 0
        for j in range(len(id_list)):
            if array[i][j] > 0:
                cnt += banned[j]
        answer.append(cnt)
    return answer