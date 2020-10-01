class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def binary(self):
        return self.items

def divby2(numb):

    s=Stack()
    while numb>0:
        rem = numb%2
        s.push(rem)
        numb = numb//2
    binstring = ''
    while not s.isEmpty:
        binstring = binstring + str(s.pop())
    return binstring

c = divby2(42)
print(c)