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



def earliest_ancestor(ancestors, start):
    #create graph dict
    graph = dict()

    #store each parent as key and child as value pair in dict
    for pair in ancestors:
        if pair[1] not in graph:
            graph[pair[1]] = set()
        graph[pair[1]].add(pair[0])
    
    #create tranverse search for the graph
    def dfs(start_vert):
        nonlocal graph
        #if no parents return -1
        if start_vert not in graph:
            return -1
        
        #make the dictionary for # of visited to reach parent
        distances = dict()
        visited = set()
        stack = Stack()
        
        stack.push([start_vert])

        #traverses
        while stack.size() > 0:
            path = stack.pop()
            vert = path[-1]
            #stacks the path to the parent and copies
            if vert not in visited:
                if vert in graph:
                    for neighbor in graph[vert]:
                        copy_path = path[:]
                        copy_path.append(neighbor)
                        stack.push(copy_path)
                        if neighbor not in graph:
                            distances[neighbor] = len(copy_path)
                            continue
                    visited.add(vert)
        results = []
        max = -1
        # finds the max number of nodes visited to find oldeest ancestor
        for k, v in distances.items():
            if v > max:
                max = v
        # adds the oldest parents to the result
        for k, v in distances.items():
            if v == max:
                results.append(k)
        # returns the smallest parent if there is a tied
        return min(results)
    return dfs(start)

