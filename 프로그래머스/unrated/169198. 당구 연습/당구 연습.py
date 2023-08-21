def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        x, y = ball
        if startX == x:
            if startY > y:
                new_balls = [[x, 2*n-y],[2*m-x, y],[-x,y]]
            else:
                new_balls = [[2*m-x, y],[x,-y],[-x,y]]
        elif startY == y:
            if startX > x:
                new_balls = [[x, 2*n-y],[2*m-x, y],[x,-y]]
            else:
                new_balls = [[x, 2*n-y],[x,-y],[-x,y]]
        else:
            new_balls = [[x, 2*n-y],[2*m-x, y],[x,-y],[-x,y]]
        result = []
        for x_new, y_new in new_balls:
            result.append((startX-x_new)**2 + (startY-y_new)**2)
        answer.append(min(result))
    return answer