# # DAY 3

# '''# -->Contant'''
# # List
# l = [1, 2, 3, 5.5, 8.3, "Satish"]
# print(l)
# print(type(l))
# print(l[0]) # get 1st index value
# print(l[1:6:2]) # [starting : ending : skip ] values
# print(l[-1]) # -1 denotes end of  the list
# print(l[::-1]) # we can get list in reverse order


# # Functios
#     # append() --> add an element to the end of the list
#     # extend() --> add all orther elements of a list to end of the list
#     # insert() --> add an element at perticular idex it have two orguments(index, value)
#     # remove() --> remove an element by value it self
#     # pop()    --> remove and return an element by index
#     # clear()  --> remove all elements from list
#     # index()  --> return value using index value
#     # count()  --> return nunber the
#     # sort()   --> return list in asconding order
#     # reverse()--> return list in reverse order
#     # copy()   --> copy the list to another varible

# l = [1, 2, 3, 5.5, 8.3, "Satish"]
# l.append("Daraboina")
# print(l)
# l.extend(["B.Tech",3,"year"])
# print(l)
# l.insert(5,9063399570)
# print(l)
# l.remove(8.3)
# print(l)
# l.pop(2)
# print(l)

# # Creat a list of 10 elements print elemnts one by one
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Method 1
# for i in range(len(l)):
#     print(l[i])

# # Method 2(using membership operator)
# for i in l:
#     print(i)


# # Create a list 5 float no. find Sum and Average
# l = [1.0, 2.5, 3.7, 9.4, 6.7]
# # Sum:
# sum = 0
# for i in l:
#     sum = i + sum
# print(sum)

# # Average:
# sum = 0
# for i in l:
#     sum = i + sum
# average = sum/len(l)
# print(average)


# # after ceating list with 6 elements from the user extract only even numbers
# size = int(input("Enter size:"))
# list = []

# for i in range(size):
#     ele = int(input("Enter element: "))
#     list.append(ele)

# for i in list:
#     if(i%2==0):
#         print("Even number in list:",i)

# '''# neon '''


# # Get list of no's as input and return their product, if product is less than 750 else return sum
# ele = list(map(int,input("Enter list of numbers: ").split()))
# product = 1
# sum = 0
# # print(type(ele))
# for i in ele:
#     product = i*product
#     sum = i+sum
# if(product<=750):
#     print("Product of elemets", product)
# else:
#     print("Sum of elemets", sum)


# '''# List Compransion'''
# n = [ele for ele in "Satish Daraboina"]
# print(n)


# l = ["hyd", "rajamaundry", "vizag", "rajanagaram"]
# city = []

# for i in l:
#     if 'r' in i:
#         city.append(i)
# print(city)

# l = [2**x for x in range(1,10)]
# print(l)


# '''# Set'''
# # not allowed duplection and denotes by '{}' brackets

# # Functions:
#     # add    --> add an element
#     # update --> add list lo elements at random position
#     # discard--> remove an element
#     # remove --> remove an element also return error if element is not present in set

# # Operations:
#     # | (or) union()      --> combain both sets
#     # & (or) intersection --> return common valuse to left side set
#     # - (or) difference   --> remove common values and return distent velues

# s = {1, 2, 3, 4, 5, 6}
# s.add(9)
# s.add(8)
# s.add(10110)
# s.update([212,55,56556])
# s.discard(212)
# s.remove(3)
# print(s)
# s.remove(3)
# print(s) #return error
# s1 = {1, 2, 3}
# s2 = {4, 5, 6, 1, 2}
# s1.union(s2)
# print(s1)


# '''Tuple'''
# # can't manupulicate the function

# t = (1,5,6,7,4,2,5,2,3,4,5,6,7,8,9,"Satish")
# print(type(t))
# print(t.count(2))
# print(t.index(5)) # for duplecate values 'index()' return first occurance value.

# '''# Dictionary'''
# #  Dictionary contains with two units (keys and values) key must me uniqe

# # Functions:
#     # keys       --> return key values of dict
#     # values     --> return values of dict
#     # items      --> return each (key and value) item simply return all pairs
#     # update     --> add one more iteam # .update({'d':55})
#     # pop        --> fetch and remove an item
#     # popitem    --> fetch and remove recently added item
#     # setdefault --> if key is not in dict - will be added or nothing will be done 

# # dict = {1:"one",2:"two"}
# # print(type(dict))
# # print(dict.keys())
# # print(dict.values())
# # print(dict.items())
# # dict.update({3:"three"})
# # print(dict)
# # dict.pop(1)
# # print(dict)
# # dict.popitem()
# # print(dict)
# # dict.setdefault(4,"four")
# # print(dict)
# # dict.setdefault(1,"four")
# # print(dict)


# type conversion list --> dict
l = ["Satish", "Daraboina"]
# dict.fromkeys(l)
# print(l)
dict.fromkeys(l)
print(l)
# dict.fromkeys(l)
# print(l)

