from math import floor, sqrt

def solution(brown, yellow):
    for h in range(1, floor(sqrt(yellow))+1):
        if yellow % h != 0:
            continue
        else:
            if brown == 2 * (h + yellow // h) + 4:
                return [yellow // h + 2, h+2]