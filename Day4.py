# # Dictionary compransion

# # Ex 1:
# dict = {n:n*n for n in range(1,5)}
# print(dict)

# # Ex 2:
# old = {'rice': 50, 'dhall': 100, 'oil': 180}
# new = {product:price*2 for(product, price) in old.items()}
# print(new)

# # Ex 3:
# real = {'ram': 40, 'raj': 24, 'sai': 33}
# now = {name:age for(name, age) in real.items() if age>30}
# print(now)

# # Create a list with 8 custmors names display a dict witch as custermor names along with discount for them from a paticular shop

# import random
# dict = ['ram', 'pavan', 'dileep', 'satish', 'murali', 'moses']
# discount = {name: random.randrange(1, 100) for name in dict}
# print(discount)
# # print(type(dict))


# # creat two lists one is students name and second as marks using thees tow list creat a list and calculate the pesentage
# students = ['ram', 'pavan', 'dileep', 'satish', 'murali', 'moses']
# marks = [410, 436, 329, 450, 390, 423]
# dict_percentage = {name: ((marks/500)*100)for (name, marks) in zip(students, marks)}
# print(dict_percentage)


'''Strings'''
# name = "Hi I'm "satish"" # invalid syntax
# print(name)

# name = 'Hi I'm satush'  # invalid syntax
# print(name)

# name = 'Hi I\'m satish'
# print(name)
# name = "Hi I'm satish"
# print(name)

# Functions:
    # upper              -->
    # lower(or) casefold -->
    # replace            -->
    # strip              -->
    # split              -->
    # center             -->
    # center             -->


s = "   satish daraboina b.tech , 3rd year.   "
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace("s","b"))
print(s.strip())
print(s.split(" "))
print(s.split("a"))
print(s.split(","))
print(s.center(8,"*"))
print(s.count("a"))
print(s.count("a",6,len(s)))
print(s.endswith("a"))
print(s.endswith("a",0,len(s)))
print(s.find("z"))
print(s.find("a",6,len(s)))
print(s.index("a"))
print(s.index("a",6,len(s)))


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
# string = input("Enter your String: ")
# i = input("Enter any element: ")
# if i in string:
#     print("Present")
# else:
#     print("Not Present")


# check given string is palandron or not?
# string = input("Enter you Stering: ")
# if string==string:
#         print("Palnodram")
# else:
#     print("not")


# After get a string as ainput check your string as space or not. if true print no. spaces in string
# s = input("Enter your string: ")
# count = 0
# for i in s:
#       if i == " ":
#             count +=1
# print(count) 


# create a list with ovels get one string as a input count ovels in the string
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
