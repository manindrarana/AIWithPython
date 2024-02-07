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
            return Exception("frontier is empty")


