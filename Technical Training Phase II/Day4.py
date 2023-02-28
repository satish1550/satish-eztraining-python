# DAY 4 --> Stacks & Queues


'''Stack'''
stack = []
def push():
    ele = int(input("Enter the element: "))
    stack.append(ele)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        ele = stack.pop()
        print("Successfully removed the", ele)
        print(stack)

while True:
    print("Select the operation", "\n", "1. Push",
          "\n", "2. Pop", "\n", "3. Quit")
    choice = int(input("Enter choice value"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Please select the correct option")




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.isempty():
            return None
        else:
            popNode = self.head
            self.head =self.head.next
            popNode.next  = None
            return popNode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        temp = self.head
        if self.isempty():
            print("Stack is empty")
        else:
            while (temp != None):
                print(temp.data, end=" ")
                temp = temp.next
                if (temp != None):
                    print("->", end=" ")
            return

if __name__ == "__main__":
    obj = Stack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.display()

    print(obj.peek())

    obj.pop()
    obj.pop()
    obj.display()




# Balanced or Not?
s = input("Enter bracess: ")
st = []
balanced = True
for char in s:
    if (char == "{" or char == "[" or char == "("):
        st.append(char)

    elif (char == "}"):
        if (len(st) and st.pop() != "{"):
            balanced = False
            break
    elif (char == "]"):
        if (len(st) and st.pop() != "["):
            balanced = False
            break
    elif (char == ")"):
        if (len(st) and st.pop() != "("):
            balanced = False
            break
    else:
        balanced = False
        break
if (balanced == False or len(st)):
    print("Not balanced")
else:
    print("Balanced")



'''Queues'''

queue = []
def enQueue():
    ele = int(input("Enter the element"))
    queue.append(ele)
    print(ele, "is added to queue..")
    print(queue)

def deQueue():
    if not queue:
        print("Queue is empty")
    else:
        ele = queue.pop(0)
        print("Successfuly removed", ele, "from Queue")
        print(queue)

while True:
    print("Select the operation \n 1. Add \n 2. Remove \n 3. Quit")
    choice = int(input("Enter the option: "))
    if choice == 1:
        enQueue()

    elif choice == 2:
        deQueue()
    elif choice == 3:
        break
    else:
        print("Please select correct option")




# Implementing Queues and Stack by using queueq mdule
from queue import LifoQueue
stack = LifoQueue(maxsize=3)

print(stack.qsize())

stack.put('A') # put func for adding / push
stack.put('B') # becouse it is a stack the out put is C | B | A (last in first out)
stack.put('C')

print(stack.full()) # return True if it is rached max size
print(stack.qsize()) # return size of the stack just like len() func
print(stack.get()) # get is just like pop() func
print(stack.get())
print(stack.get())

print(stack.empty())
print(stack.qsize())




import queue
Queue = queue.Queue(maxsize=3)
print(Queue.qsize())

Queue.put("A")
Queue.put("B")
Queue.put("C")

print(Queue.get()) # becouse it is a stack the out put is C | B | A (first in first out)
print(Queue.get())
print(Queue.get())
print(Queue.qsize())
print(Queue.empty())
print(Queue.qsize())


# Queue using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return


a_queue = Queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("quit")

    do = input("What would you like to do? ").split() # by using split , do will become a list ,split works with string

    operation = do[0].strip().lower()
    if operation == "enqueue":
        a_queue.enqueue(int(do[1]))
    elif operation == "dequeue":
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print("Queue is empty")
        else:
            print("Dequeued element :", int(dequeued))
    elif operation == "quit":
        break



# Remove Duplicates
# LOGIC:First element will be compared with rest
# then second will be compared with rest all...goes
# maintain two pointers and move
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        data = current1.data
        current2 = current1.next
        while current2:
            if current2.data == data:
                llist.remove(current2)
            current2 = current2.next
        current1 = current1.next


a_llist = LinkedList()
data_list = input("Please enter the elements in the linked list: ").split()
for data in data_list:
    a_llist.append(int(data))
remove_duplicates(a_llist)
print("The list without duplicates removed: ")
a_llist.display()