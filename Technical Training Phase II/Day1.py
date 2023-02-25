# DAY 1 


'''Lambda Function'''
# when we want to use function concept without using function name there we use lambda funcution

L = [1, 2, 3]
ans = list(map(lambda i:i+i, L))
print(ans)
ans = list(map(lambda i:i*i, L))
print(ans)

res = list(map(lambda n: pow(n,2), L))
print(res)

str = 'Satish'
(lambda str:print(str)) (str)



# Writr a program after creating a list with even numbers with in range range 1-15, now using lambda functions to create a new list which should have sqare roots?
List = []
for i in range(1,16):
    if i % 2 == 0:
        List.append(i)
print(List)
res = map(lambda res: pow(res,1/2),List) # 1/2 = sqrt
print(list(res))




'''OOPs'''
    # 1 Abstraction   --> Hiding data

    # 3 Inheritance   --> Base class and Derived class
            # Base     --> Parent class
            # Derived  --> Child class
            # Types:
                # 1 Single inheritance
                # 2 Multiple inheritance
                # 3 Multi-level inheritance
                # 4 Heirarichel inheritance
                # 5 Hybrid inheritance

    # 3 Encapsulation --> Bindind data and function into a single entity (for data security)
            # Publi     --> One class info can be accessed by any othe class
            # Private   --> Can used where it is declared or no inheritected class
            # Protected --> Can be accessed only where it got declared...which ever class inherited from this class there also we can use

    # 4 Polymorphism  --> One item or same item use for differnt purposses
           # Typs
               # 1 Overloading
                   # 1 Operating overloading  --> Same operaton use for differnt opeartions (like '+' is for addtions of two no. as well as for concation of two srtings.)
                   # 2 Method overloading     --> Same function used for differnt ways
               # 2 Overriding --> If a method is cant not be used inside Derived class it will take it from Base clss or Parent class



'''Abstraction'''
from abc import ABC, abstractmethod

class abstractdemo(ABC):
    @abstractmethod # it is called the decorator to make the method abstract
    def dispay (self):
        None
    @abstractmethod
    def show(self):
        None
# changing abstract to concrete
class demo(abstractdemo):
    def dispay(self):
        return print("Abstraction method")
    def show(self):
        return print("second function")

object = demo()
object.dispay()
object.show()



'''Inheritance'''
class parent: # BASE Class
    def disply(self):
        print('parent class')
class child(parent): # DERIVED Class
    def show(self):
        print('child class')

object = child()
object.disply()
object.show()



# single inheritance
class A:
    n = 30
class B(A):
    def calc(self):
        res = self.n+70
        print(res)
object = B()
object.calc()



# multiple inheritance
class mom:
    def mDisply(self):
        print("mom's class")
class dad:
    def dDisply(self):
        print("dad's class")
class child(mom, dad):
    def cDisply(self):
        print("child class")

object = child()
object.mDisply()
object.dDisply()
object.cDisply()



# multi-level inheritance
class grandParent:
    def gDisply(self):
        print("Grandparent's class")
class parent(grandParent):
    def pDisply(self):
        print("Parent's class")
class child(parent): # child is inheritance from parent function and parent is inheritance from grandParent
    def cDisply(self):
        print("child class")

object = child()
object.gDisply()
object.pDisply()
object.cDisply()



# heirarichel inheritance
class parent:
    def pDisply(self):
        print("Parent's class")
class child1(parent):
    def c1Disply(self):
        print("first child class")
class child2(parent): 
    def c2Disply(self):
        print("second child class")

object = child1()
object.pDisply()
object.c1Disply()
# object.c2Disply() # unable access the child2 class

object1 = child2()
object1.pDisply()
object1.c2Disply()
# object.c1Disply()  # unable access the child1 class



# hybrid inheritance
class parent:
    def pDisplay(self):
        print("Parent's class")
class child1(parent):
    def c1Display(self):
        print("child1 class")
class child2(parent):
    def c2Display(self):
        print("child2 class")
class kid1(child1):
    def k1Display(self):
        print("kid1 class")
class kid2(child1):
    def k2Display(self):
        print("kid2 class")
class son1(child2):
    def s1Display(self):
        print("son1 class")
class son2(child2):
    def s2Display(self):
        print("son2 class")

o1 = child1()
o1.pDisplay()
o1.c1Display()

o2 = child2()
o2.pDisplay()
o2.c2Display()

o3 = kid1()
o3.pDisplay()
o3.c1Display()
o3.k1Display()

o4 = kid2()
o4.pDisplay()
o4.c1Display()
o4.k2Display()

o5 = son1()
o5.pDisplay()
o5.c2Display()
o5.s1Display()

o6 = son2()
o6.pDisplay()
o6.c2Display()
o6.s2Display()




'''Encapsulation'''
# protected



# Privaate 
class encap:
    __a = 10
    def encapFunction(self):
        print("EncapFunction")
        print(self.__a)
object = encap()
object.encapFunction()



'''Polymorphism'''

'''Overloading'''

# Operator overloading
a = 10
b = 20
sum = a + b
print("Here '+' is used for addition and sum is, ", sum)
s1 = "Satish"
s2 = "Daraboina"
concat = s1 +" "+ s2
print("Here '+' is used for concatination and res is, ", concat)



# Method overloading
class moverloading:
    def display(self, a = None, b = None):
        print(a,b)
        
obj = moverloading()
print('without any arguments')
obj.display()

print('with all arguments')
obj.display(10, 20)

print('with one argiments')
obj.display(10)



'''Overriding'''
class vijayawada():
    def placeName(self):
        print("vijayawada is know as KLU")
    def student(self):
        print("yes - Vijayawada")
    def year(self):
        print("IIIrd year")
        
class hyd():
    def placeName(self):
        print("Hyd is know as HYD-KLU")
    def student(self):
        print("yes - Hyd")
    def year(self):
        print("IIIrd year")

obj_vij = vijayawada()
obj_hyd = hyd()

for details in (obj_vij, obj_hyd):
    details.placeName()
    details.student()
    details.year()