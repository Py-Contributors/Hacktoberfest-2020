class Node():
    def __init__(self, name):
        self.name = name


class Stack():
    def __init__(self):
        self.stack = []

    def add(self, node):
        self.stack.append(node)

    def contains_name(self, name):
        return any(node.name == name for node in self.stack)

    def empty(self):
        return len(self.stack) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty stack")
        else:
            node = self.stack[-1]
            self.stack = self.stack[:-1]
            return node

def main():
    # create a stack data structure
    stack = Stack()

main()
