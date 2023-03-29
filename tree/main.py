from binary_tree import Node, BinaryTree

node_a = Node('A')
print(node_a)
node_b = Node('B')
print(node_b)
node_c = Node('C')
print(node_c)
node_d = Node('D')
print(node_d)
node_e = Node('E')
print(node_e)

tree = BinaryTree()
tree.root = node_a
node_a.left_child = node_b
node_a.right_child = node_c

node_b.left_child = node_d
node_c.right_child = node_e

print('-----------------Traverse---------------')
tree.traverse(tree.root)