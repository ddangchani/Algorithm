import sys
sys.setrecursionlimit(10**6)

# Binary Tree    
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if data[0] < self.data[0]:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        
        elif data[0] > self.data[0]:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
            
    def preorder(self):
        result = []
        result.append(self.data[1])
        if self.left:
            result.extend(self.left.preorder())
        if self.right:
            result.extend(self.right.preorder())
        return result
    
    def postorder(self):
        result = []
        if self.left:
            result.extend(self.left.postorder())
        if self.right:
            result.extend(self.right.postorder())
        result.append(self.data[1])
        return result

def solution(nodeinfo):
    nodeinfo = [a + [i+1] for i, a in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x : [x[1], -x[0]], reverse=True)
    # remove y index
    for i in range(len(nodeinfo)):
        del nodeinfo[i][1]
    root = Node(nodeinfo[0])
    for i in range(1, len(nodeinfo)):
        root.insert(nodeinfo[i])
        
    pre = root.preorder()
    post = root.postorder()
    return [pre, post]