class Node():
    def __init__(self, name):
        self.name = name


class Queue():
    def __init__(self):
        self.queue = []

    def add(self, node):
        self.queue.append(node)

    def contains_name(self, name):
        return any(node.name == name for node in self.queue)

    def empty(self):
        return len(self.queue) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty queue")
        else:
            node = self.queue[0]
            self.queue = self.queue[1:]
            return node

def main():
    # create a queue
    queue = Queue()


main()
