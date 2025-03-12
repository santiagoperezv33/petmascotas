class NodeABB:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data.id < self.data.id:
            if self.left is None:
                self.left = NodeABB(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = NodeABB(data)
            else:
                self.right.add(data)

class ABB:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = NodeABB(data)
        else:
            self.root.add(data)




