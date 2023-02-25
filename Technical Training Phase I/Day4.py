# DAY 4


# Dictionary compransion
# Ex 1:
dict = {n:n*n for n in range(1,5)}
print(dict)

# Ex 2:
old = {'rice': 50, 'dhall': 100, 'oil': 180}
new = {product:price*2 for(product, price) in old.items()}
print(new)

# Ex 3:
real = {'ram': 40, 'raj': 24, 'sai': 33}
now = {name:age for(name, age) in real.items() if age>30}
print(now)



# Create a list with 8 custmors names display a dict witch as custermor names along with discount for them from a paticular shop?
import random
dict = ['ram', 'pavan', 'dileep', 'satish', 'murali', 'moses']
discount = {name: random.randrange(1, 100) for name in dict}
print(discount)
print(type(dict))



# creat two lists one is students name and second as marks using thees tow list creat a list and calculate the pesentage?
students = ['ram', 'pavan', 'dileep', 'satish', 'murali', 'moses']
marks = [410, 436, 329, 450, 390, 423]
dict_percentage = {name: ((marks/500)*100)for (name, marks) in zip(students, marks)}
print(dict_percentage)



'''Strings'''
# name = "Hi I'm "satish"" # invalid syntax
# print(name)

# name = 'Hi I'm satush'  # invalid syntax
# print(name)

name = 'Hi I\'m satish'
print(name)
name = "Hi I'm satish"
print(name)

# Functions:
    # upper          --> return the string by converting all letters into uppercase
    # lower/casefold --> return the string by converting all letters into lowercase
    # title          --> return the string by converting all all first letter in a word to uppercase 
    # replace        --> return the string by replacing letter, it's have two arrguments (repace value, repaced value)
    # strip          --> return the string by removeing all spaces at starting and ending of string
    # split          --> return the string by spliting by value or chacter in the string
    # center         --> return the string by adding leters at we want to get required length, it's have two arrguments
    # count          --> return the value of how many time a  particular char is repated in string
    # startwith      --> return the true if string is starting with given char
    # endswith       --> return the true if string is ending with given char
    # find           --> return the index value if char is prasent in string orther wise it return "-1"
    # rfind          --> return the index value from ending of the staring
    # index          --> return the index value if it present ortherwise it return error
    # islower        --> return the true if string is lower
    # isupper        --> return the true if string is upper
    # istitle        --> return the true if string is .
    # istitle        --> return the true if string is 'title-cased string(is the one in which every first letter of the word is an uppercase character)

s = "   satish daraboina b.tech ,  3rd year.   "
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.replace("s","b"))
print(s.strip())
print(s.split(" "))
print(s.split("a"))
print(s.split(","))
print(s.center(60,"%"))
print(s.count("a"))
print(s.count("a",6,len(s)))
print(s.endswith("a"))
print(s.endswith("a",0,len(s)))
print(s.find("z"))
print(s.find("s"))
print(s.rfind("s"))
print(s.find("a",6,len(s)))
print(s.index("z"))
print(s.index("a",6,len(s)))
print(s.islower())
print(s.isupper())
print(s.istitle())



'''Mutable and Immutable'''
# Mutable -->can be change after creation
    # --->list, set, dict
# Mutable -->can't be change after creation
    # --->int, float, str, bool, tuple

a = 10
print(a)
print(id(a))
a = 20
print(id(a))
print(a)



# get one string as a input along with no. find out and display weather it is present in string or not?
string = input("Enter your String: ")
i = input("Enter any element: ")
if i in string:
    print("Present")
else:
    print("Not Present")



# check given string is palandron or not?
string = input("Enter you Stering: ")
if string==string:
        print("Palnodram")
else:
    print("not")



# After get a string as ainput check your string as space or not. if true print no. spaces in string?
s = input("Enter your string: ")
count = 0
for i in s:
      if i == " ":
            count +=1
print(count)



# Create a list with ovels get one string as a input count ovels in the string?
ovels = ['a', 'e', 'i', 'o', 'u']
count = 0
listOfOvels = []
s = input("Enter your string: ")
for i in s:
    if i in ovels:
        listOfOvels.append(i)
        count+=1
print(listOfOvels)
print(count)



'''# Math Module'''
import math
print("Cell 12.5:", math.ceil(12.5))
print("Floor 12.5:", math.floor(12.5))
print("SQRT 12.5:", math.sqrt(12.5))
print("Factoral 12:", math.factorial(12))
print("Power 12,3:", math.pow(12,3))
print("Remainder 10,4", math.fmod(10,4))

a,b = divmod(10,3)
print(a,b)
