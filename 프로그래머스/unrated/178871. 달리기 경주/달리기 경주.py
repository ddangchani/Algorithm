def solution(players, callings):
    player_dict = {v : i for i,v in enumerate(players)}
    rank_dict = {i : v for i,v in enumerate(players)}
    
    for call in callings:
        idx = player_dict[call] # ranking
        previous = rank_dict[idx-1] # name
        
        # change player_dict
        player_dict[call] -= 1
        player_dict[previous] += 1
        
        # change rank_dict
        rank_dict[idx] = previous
        rank_dict[idx-1] = call
        
    result = [a[1] for a in sorted(rank_dict.items())]
        
    return result