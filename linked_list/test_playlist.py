from linked_list_playlist import Node, LinkedList


# Nodes instantiation
node_0 = Node((1000, 'Aguacero', 'Bad Bunny', 'Un Verano Sin Ti'))
node_1 = Node((1004, 'Mañana', 'Ozuna', 'OzuTochi'))
node_2 = Node((1008, 'PUNTO 40', 'Rauw Alejandro', 'SATURNO'))
node_3 = Node((1012, 'MAMIII', 'Becky G', 'ESQUEMAS'))
node_4 = Node((1016, 'La Bachata', 'Manuel Turizo', 'La Bachata'))
node_5 = Node((1020, 'PUNTO G', 'Quevedo', 'DONDE QUIERO ESTAR'))
node_6 = Node((1024, 'La Jumpa', 'Arcangel', 'La Jumpa'))
node_7 = Node((1028, 'DESPECHA', 'ROSALIA', 'DESPECHA'))
node_8 = Node((1032, 'Brother', 'Anuel AA', 'LLNM2'))
node_9 = Node((1036, 'X', 'Nicky Jam', 'Intimo'))

# Node in memory
# print(node_a)
# print(id(node_a))

# Create LL
ll = LinkedList()
print(ll)

# Insert at beginning
ll.insert_at_beginning(node_0)
ll.insert_at_beginning(node_1)
ll.insert_at_beginning(node_2)
ll.insert_at_beginning(node_3)
ll.insert_at_beginning(node_4)
ll.insert_at_beginning(node_5)
ll.insert_at_beginning(node_6)
ll.insert_at_beginning(node_7)
ll.insert_at_beginning(node_8)
ll.insert_at_beginning(node_9)
print(ll)

ll.control()
