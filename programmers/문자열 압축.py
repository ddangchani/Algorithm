def solution(s):
    max_len = max(len(s) // 2, 1)
    answers = []
    for i in range(1,max_len+1): # 길이 1일때 주의!
        cnt = 0
        ls = []
        while cnt < len(s) // i:
            ls.append(s[cnt*i:(cnt+1)*i])
            cnt +=1
        if len(s) % i != 0:
            ls.append(s[cnt*i:])
        new_idx = 0
        nums = []
        strs = []
        num = 0
        for j in range(len(ls)):
            if ls[j] == ls[new_idx]:
                num += 1
            else:
                nums.append(num)
                strs.append(ls[new_idx])
                new_idx = j
                num = 1
        nums.append(num)
        strs.append(ls[new_idx])
        length = 0
        for idx,val in enumerate(nums):
            if val != 1:
                length += len(str(val)+strs[idx])
            else:
                length += len(strs[idx])
        answers.append(length)
        
    return min(answers)