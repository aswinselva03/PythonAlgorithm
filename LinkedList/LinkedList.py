class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str("Node")

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
        # increment the length of LL and return True(will be used in another function)
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
        new_node = Node(value)
        # if LL is empty just assign head and tail to new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # else, self.head is the first node, assign self.head to new_node.next and shift self.head as new node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        # we need to return the removed element so assign temp with self.head
        temp = self.head
        # move head to the next node in LL
        self.head = self.head.next
        # detach temp by assigning temp.next = None
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        # if out of bound
        if index < 0 or index >= self.length:
            return None
        # we need to return node so assign head to temp and loop to get to the index position
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        # use get to get the node at index, if node is not none, set the value
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # index out of bound
        if index < 0 or index>self.length:
            return False
        # when you have to insert as the first node, do prepend
        if index == 0:
            return self.prepend(value)
        # when you have to insert as the last node, do append
        if index == self.length:
            return self.append(value)
        # Any other position, get the node before index position and swap next values
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    
    def remove(self, index):
        if index < 0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after




        

my_linked_list = LinkedList(4)
print("appending 2")
my_linked_list.append(2)
print(my_linked_list)
print("popping 2",my_linked_list.pop())
print(my_linked_list)
print("prepending 2", my_linked_list.prepend(2))
print(my_linked_list)
print("pop_first 2", my_linked_list.pop_first())
print(my_linked_list)
print("pop_first 4", my_linked_list.pop_first())
print(my_linked_list)
print("appending 2", my_linked_list.append(2))
print("appending 4", my_linked_list.append(4))
print(my_linked_list)
print("Get index 2",my_linked_list.get(2))
print("Get index 0",my_linked_list.get(0))

print("set index 0",my_linked_list.set(0,5))
print(my_linked_list)
print("set index 2",my_linked_list.set(2,5))
print(my_linked_list)
my_linked_list.insert(0, 3)
my_linked_list.insert(2,1)
print(my_linked_list)
my_linked_list.remove(0)
print(my_linked_list)
print(my_linked_list.reverse())
print(my_linked_list)