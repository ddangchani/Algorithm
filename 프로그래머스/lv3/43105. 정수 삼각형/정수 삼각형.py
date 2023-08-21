def solution(triangle):
    row = triangle.pop(0)
    while triangle:
        ls = triangle.pop(0)
        new_row = [0] * len(ls)
        for i, v in enumerate(ls):
            if i == 0:
                new_row[0] = row[0] + v
            elif i == len(ls) - 1:
                new_row[i] = row[i-1] + v
            else:
                new_row[i] = max(row[i-1], row[i]) + v
        row = new_row
    
    return max(row)