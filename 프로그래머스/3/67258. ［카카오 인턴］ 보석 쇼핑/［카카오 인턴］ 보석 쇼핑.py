def solution(gems):
    gemset = set(gems) 
    n = len(gemset) # number of total kinds
    N = len(gems)
    left, right = 0, 0
    bl, br = 0, N-1
    gemdict = {gems[0] : 1}
    print(N, n)
    
    while left <= right and right <= N-1:
        current = len(gemdict.keys())
        if current < n:
            if right < N-1:
                if gems[right+1] in gemdict.keys():
                    gemdict[gems[right+1]] += 1
                else:
                    gemdict[gems[right+1]] = 1
                
                right += 1
            else:
                break
        else:
            if right - left < br - bl:
                bl, br = left, right
                
            if gemdict[gems[left]] == 1:
                del(gemdict[gems[left]])
            else:
                gemdict[gems[left]] -= 1
            left += 1
        # print(left, right, gemdict)
        
    return [bl+1, br+1]