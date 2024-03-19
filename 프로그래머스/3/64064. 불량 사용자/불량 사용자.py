# Bruteforce
from itertools import product, permutations

def match(ban, user_id):
    ans = []
    cnt_ast = ban.count('*')
    cnt = 0
    if len(ban) != len(user_id):
        return False
    for j in range(len(user_id)):
        if user_id[j] != ban[j]:
            cnt += 1
    if cnt == cnt_ast: 
        return True
    return False
        

def solution(user_id, banned_id):
    ans = set()
    for i, perm in enumerate(permutations(user_id, len(banned_id))):
        to_append = True
        for usr, ban in zip(perm, banned_id):
            if not match(ban, usr):
                to_append = False
        if to_append:
            ans.add(tuple(sorted(list(perm))))
    
    return len(ans)
    
    