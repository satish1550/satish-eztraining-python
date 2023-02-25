# DAY 6 


'''Exception'''
    # When ther is exception the developer doee not want intraption/distabane in the program flow to achive this we are using Exception


a = 10
# b = 0
b = 1
try: # you are trying to compail, it may have errors.
    print(a/b)
except Exception as e: # if any error are occur this can handle
    print("Sorry it is not possible",e) # 'e' can print what is error.!
finally:  # To check program execution goes till end or getting any error it not executed
    print("successfuly executed")



#Like specialised doctors
# for those specific error onlt those exception blocks will be get executed
a = 10
try:
    b = int(input("Enter b value: "))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("Number can't be divisibly zero,", e)
except ValueError as e:
    print("Invalid error,", e)
except Exception as e:
    print("Other error:", e)
finally:
    print("resource closed")



# raise used to interrupt normal program flow and raise
a = int(input("Enter a value: "))
if a % 2 != 0:
    raise Exception(a, "should be even number")
else:
    print(a, "is even number..correct")



'''OOPs'''
    # Object Oriented Programming(OOPs)
    # It's an effienct concept use all program
    # For multepul reasons we use opps concept for example Code Reusability, Data Scurity and Data Hyding

    # '''CLASS'''
        # it an 
    # '''OBJECT'''
        # it's a thing based on class

    # NOTE: One class has a multiple objects

    # Example 1:
        # class: Birds
        # objects: peacock, parrots, owls, etc.

    # Example 2:
        # class: Laptops
        # objects: HP, Lenovo, Dell, etc.



class computer: # class def 
    def config(self): # config is a user define function
        print("YES")

lenovo = computer() # object
lenovo.config() # asseccing funtion

dell = computer()
dell.config()



class Employe:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))

emp1 = Employe("Satish", 369)
emp2 = Employe("Dileep", 364)
# emp3 = Employe(364, "Dileep")
# emp4 = Employe(369, "Satish")

emp1.display()
emp2.display()
# emp3.display()
# emp4.display()



# varibles and var.access in class and method
class computer:
    a = 10 # global scop
    b = 20 # global scop
    print("class varible inside class", a, b)

    def config(self):
        c = 100 # local scop
        print("YES")
        print("Instance access", self.a) # we can access global var

lenova = computer()
print(lenova.a)
# print(lenova.c) # not accessing
print(lenova.a + lenova.b)
lenova.config()

dell = computer()
print('dell', dell.b)



