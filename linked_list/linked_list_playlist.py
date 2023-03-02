import random

class Node:
    '''
    Node object.
    Args:
        data (str): string value to store in node
    Attributes:
        data (str): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None


    def __repr__(self):
        return '{}'.format(self.data)
    
    def get_data(self):
        return self.data


class LinkedList:
    '''
    Linked List object.
    Args:
        None
    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None
        self.actual = None


    def __iter__(self):
        node = self.start
        self.actual = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = [("START",)]

        for node in self:
            nodes.append(node.data)

        nodes.append(("NIL",))
        return " <--> ".join(str(node) for node in nodes)


    def traverse(self):
        '''
        Navigates every node in the list.
        Args:
            None
        Returns:
            None
        '''
        
        current_node = self.actual

        while current_node is not None:
            current_node = current_node.next
            return current_node
    

    def show_details(self):
        print('|__________Details__________|')
        print('|__ID: {}__|'.format(self.actual.get_data()[0]))
        print('|__NAME: {}__|'.format(self.actual.get_data()[1]))
        print('|__ARTIST: {}__|'.format(self.actual.get_data()[2]))
        print('|__ALBUM: {}__|'.format(self.actual.get_data()[3]))
        self.control()
    

    def play(self):
        print()
        print('|___Reproducing Song {} from {}___|'.format(self.actual.get_data()[1], self.actual.get_data()[2]))
        self.control()


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.
        Args:
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        new_node.next = self.start
        if self.start is not None:
            self.start.prev = new_node
        self.start = new_node


    def length(self):
        current = self.start
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    

    def playlist_songs(self):
        count = self.length()
        print()
        print('|__The playlist have {} songs__|'.format(count))
        self.control()
    

    def Next(self):
        current_node = self.actual
        if current_node is not None:
            current_node = current_node.next
            self.actual = current_node
            self.play()
            self.control()


    def previous(self):
        current_node = self.actual
        if current_node is not None:
            prev_node = current_node.prev
            if prev_node is not None:
                self.actual = prev_node 
                self.play()
                self.control()


    def shuffle(self):
        if self.length() == 0:
            return None

        index = random.randint(0, self.length()-1)

        current = self.start
        for i in range(index):
            current = current.next

        self.actual = current
        self.play()


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.
        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current_node
                current_node.prev = new_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.
        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def search(self):
        '''
        Searches for a node given a value reference.
        Args:
        reference_node (str): value of node used as reference

        Returns:
        node (Node): node found or None
        '''
        current = self.start
        count = 1

        val = input('|__Write the song name or the artist: ')
        print('| Searching..... |')

        while current != None:
            if current.get_data()[count] == val:
                self.actual = current
                self.play()
                self.control()
                return
            
            if count < 2:
                count += 1

            else:   
                current = current.next
                count = 1
 
        print('{} not found in playlist...  :C '.format(val))
        self.control()


    def control(self):
        flag = True
        while flag == True:
            print()
            print('1. Previous song')
            print('2. Play song')
            print('3. Next song')
            print('4. Details of the song')
            print('5. Search song')
            print('6. Shuffle')
            print('7. Number of the songs')
            print()

            inp = input('|__Selecciona una opcion: ')
            print()

            if inp == '1':
                self.previous()
            elif inp == '2':
                self.play()
            elif inp == '3':
                self.Next()
            elif inp == '4':
                self.show_details()
            elif inp == '5':
                self.search()
            elif inp == '6':
                self.shuffle()
            elif inp == '7':
                self.playlist_songs()
            else:
                print('|____Opcion invalida, por favor selecciona otra vez____|')
                print()