class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str({"value":self.value,
                    "next": self.next})

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __str__(self):
        linked_list = ""
        temp = self.head
        if temp is None:
            return "None"
        for _ in range(0, self.length+1):
            linked_list += str(temp.value)
            linked_list += "->"
            if temp.next is None:
                linked_list += "None"
                return linked_list
            temp = temp.next
        return linked_list
            
    
    def append(self, value):
        new_node = Node(value)
        # if the linked list is empty assign head and tail to new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if not, assign, tail.next  as new node(now None) and then shift tail to the new node(already new_node.next is None)
        else:
            self.tail.next = new_node
            self.tail = new_node
        # increment the lenght of LL and return True(will be used in another function)
        self.length +=1
        return True
    
    def pop(self):
        # if length is 0, return None
        if self.length == 0:
            return None
        # we are using pre and temp, to find the node before tail (if doubly linked list we can do a prev in tail to get that)
        # here we need to do it ourselves
        pre = self.head
        temp = self.head
        # our goal is to find new tail(since pop removes the last node, node before last node is our new tail)
        while(temp.next): # until temp.next is not none - temp is not the tail
            prev = temp # retaining the previous node of tail in prev
            temp = temp.next
        prev.next = None
        self.tail = prev
        self.length -= 1
        # for cases when we have only one node in LL, the node will not be removed from above steps so
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # the last element removed should be returned


    def prepend(self, value):
        pass

    def insert(self, position, value):
        pass
    
    def remove(self, position, value):
        pass

my_linked_list = LinkedList(4)
print("appending 2")
my_linked_list.append(2)
print(my_linked_list)
print("popping 2",my_linked_list.pop())
print(my_linked_list)

        