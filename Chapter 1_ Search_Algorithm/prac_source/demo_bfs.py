import sys

class Node():
    def __init__(self, actions, parent, state):
        self.actions = actions
        self.parent = parent
        self.state = state


class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self,node):
        self.frontier.append(node)
    
    def contains_node(self,state):
        return any(node.state == state for node in self.frontier )
    
    def check_empty(self):
        if self.empty():
            return len(self.frontier) == 0
    
    def remove(self):
        if self.check_empty():
            return Exception("frontier is empty")
        else:
            return self.frontier.pop(0)
        

class Maze():
    def __init__(self,filename):
        self.filename = filename

        with open (filename) as f: 
            content = f.read()
        
        if content.count('A') !=1: 
            raise Exception ("should atleaast have a starting point")

