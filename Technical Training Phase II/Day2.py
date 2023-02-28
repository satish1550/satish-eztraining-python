# DAY 2


'''DSA'''
    # Data Structures and Algorithms
    # It helps to write the efficent programs
    # Linear --> Arrays, linked List , Stack, Queue, Matrix
    # Non Linear --> Binary Tree, Heap, Hash Table, Graph

# Data Structures
    # Linear:
        # Statc --> Array (Fixed Size)
        # Dynamic --> List, Stack, Queue (No Fixed Size)
    # Non Linear:
        # Graph
        # Tree



'''LINKED LIST'''
    # real time example: Train
    # As the name says link with one and another is called Linked List
    # Types:
        # Single Linked List / Singly
        # double Linked List / Doubly
        # ctrcular Linked List
    # Opeartions:
        # Insert
            # At the Begining
            # At the End
            # At the Position
        # Delete
        # Search


'''Single Linked list'''
# Crating a Single Linked list
    # step 1 --> create a Node
    # step 2 --> parteshion the Node with two sigments Data and None
    # step 3 --> Add value into the blank Node
    # step 4 --> Mark the Node as Head
    # step 5 --> Create the next Node by following the above stpe
    # step 6 --> Establish the link between the first Node and Second Node

# Displaying the Linked List:
    # Traveasy is required to from first Node till Node in order to display linked list


# Ex 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty..!")
        else:
            temp = self.head # temp = first Node
            while temp:
                print(temp.data, "->", end=" ") #
                temp = temp.next # establishing ink the first Node to next Node
                
obj = singleLinkedList()
# Node creation / Initialising
n = Node(10) # n.data in Node class will be 10
obj.head = n # Assigning first Node as Head
n1 = Node(20)
obj.head.next = n1 # next Node value
n2 = Node(30)
n1.next = n2
obj.display()



# Ex 2:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class singleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty..!")
        else:
            temp = self.head # temp = first Node
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
                
obj = singleLinkedList()
w = Node("W")
obj.head = w
i = Node("I")
obj.head.next = i
n1 = Node("N")
i.next = n1
n2 = Node("N")
n1.next = n2
e = Node("E")
n2.next = e
r = Node("R")
e.next = r
obj.display()



'''Opeartions:'''
# Inserting
# Inserting at the Begining
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def display(self):
        if self.head is None:
            print("The List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next

obj = singleLinkedList()
n1 = Node(20)
obj.head = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
print("List before inserting 10 at begining")
obj.display()
print("")
print("List after inserting 10 at begining")
obj.insert_begining(10)
obj.display()



# Inserting at the End
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singleLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def display(self):
        if self.head is None:
            print("The List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next

obj = singleLinkedList()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
print("List before inserting 50 at end")
obj.display()
print("")
print("List after inserting 50 at end")
obj.insert_end(50)
obj.display()



# Inserting at the Postion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_position(self, pos, data):
        new = Node(data)
        temp = self.head
        
        for i in range(pos-1):
            temp = temp.next
            new.next = temp.next
            temp.next = new
        
    def display(self):
        if self.head is None:
            print("The List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "->", end=" ")
                temp = temp.next

obj = singleLinkedList()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
print("List before inserting 30 at index 2")
obj.display()
print("")
print("List after inserting 30 at index 2")
obj.insert_position(2, 30)
obj.display()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head

        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next


List = LinkedList()
n = int(input("How many elements you like to ...?"))
for i in range(n):
    data = int(input("Enter data item :"))
    List.append(data)
print("The linked list is ", end=" ")
List.display()