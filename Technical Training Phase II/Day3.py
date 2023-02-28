# DAY 3


# Cerating the Linked List with accending order, inserting and deleting
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def dispaly(self):
        current = self.head
        if not current:
            print("Linked List is", current, "/ empty")
        else:
            print("Start ->", end=" ")
            while current:
                print(current.data, '->', end=" ")
                current = current.next
            print("end.")

    def insert(self, data):  # inserting in accending order
        newNode = Node(data)
        if self.head is None:  # if the Node is empty
            self.head = newNode

        elif self.head.data >= newNode.data:  # if the data is samller then head
            newNode.next = self.head
            self.head = newNode

        else:
            temp = self.head
            while temp.next and newNode.data > temp.next.data:  # locate the Node befor inserting
                temp = temp.next
                newNode.next = temp.next  # Inserting
                temp.next = newNode

    def delete(self, key):
        if self.head is None:  # if the list is empty
            print("Deletion Error: The list is", self.head, "/ empty")
            return

        if self.head.data == key:  # if the key is in head
            self.head = self.head.next
            return

        current = self.head
        while current:  # finding position of the first occurrence of the
            if current.data == key:
                break
            previous = current
            current = current.next

        if current is None:
            print("Deletion Error: Key:", key, "is not found")
        else:
            previous.next = current.next
            print("Successfuly deleted:", current.data)
            print("")


if __name__ == "__main__":
    obj = linkedList()
    print("")
    obj.insert(40)
    obj.insert(30)
    obj.insert(50)
    obj.insert(20)
    obj.insert(10)

    obj.dispaly()

    print("")
    obj.delete(30)
    obj.delete(0)
    print("")
    obj.dispaly()
    print("")


# Creating own modules
import Day2 # Day2 in my another file acting as a module hear
Day2.singleLinkedList()
print(__name__)

print("Before Function")
def f1():
    print("F1")
def f2():
    print("F2")
def f3():
    print("F3")
    
if __name__ == "__main__":
    f1()
    f2()
    f3()
print("Name:", __name__)


'''Double LinkedList'''

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("The list is", self.head, "/ empty")
        
        else:
            temp = self.head
            print("Start", end=" ")
            while temp:
                print(temp.data, "<->", end=" ")
                temp = temp.next
            print("end.")

obj = doubleLinkedList()
print("")
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3

obj.display()
print("")




# Inserting in Double Linked List
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insertBegining(self, data):
        newNode = Node(data)
        temp = self.head
        temp.prev = newNode
        newNode.next = temp
        self.head = newNode
        
    def insertEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp  
        
    def insertPosition(self, pos, data):
        newNode = Node(data)
        temp = self.head
        for i in range(0, pos-1):
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        
    def display(self):
        if self.head is None:
            print("The list is", self.head, "/ empty")
        
        else:
            temp = self.head
            print("Start", end=" ")
            while temp:
                print(temp.data, "<->", end=" ")
                temp = temp.next
            print("end.")

obj = doubleLinkedList()
print("")
n1 = Node(20)
obj.head = n1
n2 = Node(30)
n2.prev = n1
n1.next = n2
n3 = Node(40)
n3.prev = n2
n2.next = n3

#  At begining
print("List before inserting 10 at begining")
obj.display()
print("")
print("List after inserting 10 at begining")
obj.insertBegining(10)
obj.display()
print("")

#  At end
print("List before inserting 50 at end")
obj.display()
print("")
print("List after inserting 50 at end")
obj.insertEnd(50)
obj.display()
print("")

#  At position
print("List before inserting 25 at index 2")
obj.display()
print("")
print("List after inserting 25 at index 2")
obj.insertPosition(2, 25)
obj.display()
print("")




# deleteing in Double Linked List
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        
    def deleteBegining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        
    def deleteEnd(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        
    def deletePosition(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
        
    def display(self):
        if self.head is None:
            print("The list is", self.head, "/ empty")
        
        else:
            temp = self.head
            print("Start", end=" ")
            while temp:
                print(temp.data, "<->", end=" ")
                temp = temp.next
            print("end.")

obj = doubleLinkedList()
print("")
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n2.prev = n1
n1.next = n2
n3 = Node(30)
n3.prev = n2
n2.next = n3
n4 = Node(40)
n4.prev = n3
n3.next = n4
n5 = Node(50)
n5.prev = n4
n4.next = n5

#  At begining
print("List before deleteing 10 at begining")
obj.display()
print("")
print("List after deleteing 10 at begining")
obj.deleteBegining()
obj.display()
print("")

#  At end
print("List before deleteing 50 at end")
obj.display()
print("")
print("List after deleteing 50 at end")
obj.deleteEnd()
obj.display()
print("")

#  At position
print("List before deleteing 30 at index 2")
obj.display()
print("")
print("List after deleteing 30 at index 2")
obj.deletePosition(1)
obj.display()
print("")



'''Circular Linked List'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        
    def add(self, data): # adding node at the end of Linked List
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
            
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head # we point the tail to the head since it is circular Linked List
            
    def display(self):
        if self.head is None:
            print("List is empty..!")
        else:
            temp = self.head
            print(temp.data, "-->") 
            while (temp.next != self.head):
                temp = temp.next
                print(temp.data, "-->")
                
class createList:
    obj = circularLinkedList()
    obj.add("S")
    obj.add("A")
    obj.add("T")
    obj.add("I")
    obj.add("S")
    obj.add("H")
    obj.display()