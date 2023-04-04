class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __str__(self):
        linked_list = ""
        if self.head == None:
            return "None"
        for _ in range(0, self.length+1):
            
            linked_list += str(self.head.value)
            linked_list += "->"
            if self.head.next == None:
                linked_list += "None"
                return linked_list
            self.head = self.head.next
        return linked_list
            
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        pass

    def insert(self, position, value):
        pass
    
    def remove(self, position, value):
        pass

my_linked_list = LinkedList(4)
my_linked_list.append(2)
print(my_linked_list)
        