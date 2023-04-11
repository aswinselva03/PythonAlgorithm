class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def __str__(self):
        doubly_linked_list = "None<-"
        temp = self.head
        if temp is None:
            return "None"
        for _ in range(0, self.length+1):
            doubly_linked_list += str(temp.value)
            if temp.next is None:
                doubly_linked_list += "->None"
                return doubly_linked_list
            doubly_linked_list += "<=>"
            temp = temp.next
        return doubly_linked_list

dll = DoublyLinkedList(5)
dll.append(2)
dll.append(10)
dll.pop()
print(dll)