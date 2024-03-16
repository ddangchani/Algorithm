from heapq import heappop, heappush

def solution(operations):
    maxheap, minheap, result = [], [], []
    # default : minheap in python!
    
    for operation in operations:
        oper, num = operation.split(' ')
        num = int(num)
        if oper == 'I':
            heappush(minheap, num)
            heappush(maxheap, num * (-1))
        else:
            if num == -1:
                if len(minheap) > 0:
                    x = heappop(minheap)
                    maxheap.remove(x * (-1))
            else:
                if len(maxheap) > 0:
                    x = heappop(maxheap)
                    minheap.remove(x * (-1))
                
    # Answer
    if len(minheap) == 0:
        return [0,0]
    else:
        return [(-1)*heappop(maxheap), heappop(minheap)]