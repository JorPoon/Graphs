from collections import deque
'''
Edge Cases:
Returns -1 if no parents
No repetition, only one path to parents
'''
class Stack():
    def __init__(self):
        self.stack = deque()
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)



def earliest_ancestor(input):
    #
    #returns -1 if no parent, output = -1
    #if earliest ancetor is tied returns smaller num
    #earliest ancestor as return value
    pass