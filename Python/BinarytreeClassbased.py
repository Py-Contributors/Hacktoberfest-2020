class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)

                else:
                    self.right.insert(data)
        else:
            self.data = data

c1 = Node(14)
c1.insert(42)
c1.insert(16)
c1.insert(8)
            
