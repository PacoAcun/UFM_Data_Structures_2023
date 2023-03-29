class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self) -> str:
        return '({})'.format(self.data)
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse(self, node):
        print(node)
        if node.left_child != None:
            self.traverse(node.left_child)

        if node.right_child != None:
            self.traverse(node.right_child)
