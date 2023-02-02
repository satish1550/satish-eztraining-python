# DAY 1 INTRODUCTION TO PYTHON...

# Printing Our Name in Telugu
print(chr(3105)+chr(3135) + " ."+chr(3128)+" "+chr(3108)+chr(3135)+" "+chr(3127)+chr(3149))


# 1num = 55  '''Not start with number and any special character expect:"_" (underscore)''
# print(1num)


'''Data type'''
# Numarics:
num1 = 55
print(num1)
print(type(num1))

_num2 = 54.59
print(_num2)
print(type(_num2))


# Complex numbers:
num3 = 43+5j
print(type(num3))


# Boolens:
num4 = True
print(type(num4))

num5 = False
print(type(num5))

Bool1 = bool(1)
print(Bool1)

Bool2 = bool(0)
print(Bool2)


# String:
num6 = "Satish"
print(type(num6))


# List:
num7 = [[1, 2, 3], [4, 5, 6]]
print(type(num7))


# Tuple:
num8 = (1, 2, 3)
print(type(num8))


'''Type Convertion'''
# Float -> Int
num9 = int(35.4)
print(num9)
print(type(num9))

# Int -> Float
num10 = float(35)
print(num10)
print(type(num10))

# Int -> Str
num11 = str(55)
print(type(num11))

# Str -> Int
num12 = int("123")
print(num12)
print(type(num12))

# Str -> Float
num12 = float("55")
print(num12)
print(type(num12))

# id address
num13 = id(55)
print(num13)


# Ardhamatic Operators
      # "+" --> Addition
      # "-" --> Subraction
      # "/" --> Division returns Qocent  Float
      # "//" --> Division return coqucent Integer (Floor Division)
      # "%" --> Division returns reminder


# Q1
print("Kumar having :", (75/2)+(37.5/2))
print("Sam having :", 37.5/2)


# Q2
print(((3*36.32)+56.19)-10)


# Q3 Multiplycation of one +ve no. with _ve float no.
positive = int(input())
negative = -float(input())
print(positive*negative)


# Q4
F1 = float(input())
F2 = float(input())
F3 = float(input())
print(F1+F2+F3)


# Q5
print(F1/F2)


# Comparisions Operator
      # == --> equls to
      # != --> not equls to
      # >  --> grater than
      # >  --> grater than
      # <  --> less than
      # <  --> less than

print(10 == 10)  # True
print(10 != 2)  # True
print(10 == 10)  # True
print(10 == "10")  # False
print(10 > 2)  # True
print(10 < 2)  # False


# Logical Operators
      # and --> return "True" if both conditions are true
      # or --> return "True" if any one condition is true
      # not --> return oppsite boolen

print(10 > 1 and 3 < 4)  # True
print(10 < 20 and 20 > 10)  # True
print(10 < 20 and 20 < 10)  # False
print(10 > 20 and 20 < 10)  # False

print(10 < 20 or 20 < 10)  # True
print(10 > 20 or 20 < 10)  # False

print(not (10 == 10))  # False
print(not (10 == 11))  # True


# Multiple inputs in same line
a, b = int(input("Enter A value: ")), int(input("Enter B value:"))
print(a)
print(b)
Sum = a+b
print(a, "+", b, "=", Sum)


# using split function
A, B = input("Enter A,B values").split(",")
print(A)
print(B)
Sum1 = A+B
print(Sum1)


# --> Change three integer no. three float no. and two string and one complex no.
      # Note: use formated input.!

Num1 = int(input("Enter first Integer :"))
Num2 = int(input("Enter second Integer :"))
Num3 = int(input("Enter third Integer :"))
print("")
Num4 = float(input("Enter first Float :"))
Num5 = float(input("Enter second Float :"))
Num6 = float(input("Enter third Float :"))
print("")
Num7 = input("Enter first String :")
Num8 = input("Enter second String :")
print("")
Num9 = complex(input("Enter Compelx :"))

print("First Integer:", Num1)
print("Second Integer:", Num2)
print("Third Integer:", Num3)
print("")
print("First Float :", Num4)
print("Second Float :", Num5)
print("Third Float :", Num6)
print("")
print("First string: ", Num7)
print("Second string: ", Num8)
print("")
print("Complex Number: ", Num9)


# --> Swaping with temp value
a = 10
b = 5
print("Vales before Swaping")
print(a)
print(b)
temp = a  # temp=10
a = b  # a=5
b = temp  # b=10
print("After Swaping")
print("a value after swaping is:", a)
print("b value after swaping is:", b)


# --> Swaping without temp value
a = 10
b = 5
print("Vales before Swaping")
print(a)
print(b)
a = a+b  # a=15
b = a-b  # b=
a = a-b  #
print("After Swaping")
print("a value after swaping is:", a)
print("b value after swaping is:", b)


# --> Area & perimeter of a rectiangle
l = int(input("Enter Length of the Rectiangle: "))
b = int(input("Enter Width of the Rectiangle: "))
area = l*b
perimeter = 2*(l+b)
print("Perimeter of Rectiangle is", perimeter)
print("Area of Rectiangle is", area)