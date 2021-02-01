class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        elem = self.stack[-1]
        del self.stack[-1]
        return elem

    def peek(self):
        return self.stack[-1]
