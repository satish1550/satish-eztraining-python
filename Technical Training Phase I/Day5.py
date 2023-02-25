# DAY 5 


import random as r
x=" i love sweets"
print (r.sample(x,3))


# Everytime it gives different output
import random as r
a = [1,2,3,4,5,6]
r.shuffle(a)
print (a)

a = [1,2,3,4,5,6]
print (r.choice(a))

b = "welcome back"
print(r.choice(b))

a = r.random() # Gives random float values from 0 -> 1
print(a)

a = r.random()+1 # Add one to ramdom no. so we get required range.
print(a)



# To find out all the functions in a module
import random as r
z = dir(r)
print(z)



# Display whole year calendar
import calendar
print("Full Calendar")
print(calendar.calendar(2023))

print("Particular Month")
print(calendar.month(2023, 2))

print("Set first day of the week")
calendar.setfirstweekday(calendar.MONDAY)
print(calendar.month(2023, 12))


# Date time moudle
import datetime
a = datetime.datetime.now()
print(a)

year = a.strftime("%Y")  # upper case Y
print("year short version:", year)

year = a.strftime("%y")   # lower case y
print("year full version:", year)



'''# Functions'''
# classfcation
# For code reuseabailty inmuitlable we can write it once include that and can call the function
# Types :-
    # 1)functions with arrugment, without return value
    # 2)functions with arrugment, with return value
    # 3)functions without arrugment, without return value
    # 4)functions without arrugment, with return value

def sample():
    print("collage days")
    print("real days")
sample()
print("today")
sample()  # Recall the function.!
print("present days")
sample()
print("class room")



# Without arugument, without return value
def multi():
    n1 = int(input("Enter n1 value: "))
    n2 = int(input("Enter n2 value: "))
    n3 = int(input("Enter n3 value: "))
    prod = n1*n2*n3
    print("product of", n1, "*", n2, "*", n3, "=", prod)
multi()



# Without arugument, with return value
def multi():
    n1 = int(input("Enter n1 value: "))
    n2 = int(input("Enter n2 value: "))
    n3 = int(input("Enter n3 value: "))
    prod = n1*n2*n3
    # ans = print("product of", n1, "*", n2, "*", n3, "=", prod)
    return prod
res = multi()
print("product is:", res)



# With arugunment,without return value
# static input
def multi(n1, n2, n3):
    prod = n1*n2*n3
    ans = print("product of", n1, "*", n2, "*", n3, "=", prod)
    return (ans)

res = multi(3, 4, 5)


# user input
def multi(a,b,c):
    prod = a*b*c
    ans = print("product of", n1, "*", n2, "*", n3, "=", prod)
    return(ans)
n1 = int(input("Enter n1 value: "))
n2 = int(input("Enter n2 value: "))
n3 = int(input("Enter n3 value: "))
res = multi(n1,n2,n3)



# With arugunment,with return value
#static input
def multi(n1, n2, n3):
    prod=n1*n2*n3
    return prod

res=multi(3, 4, 5)
print("produt is:",res)


# user input
def multi(a,b,c):
    prod = a*b*c
    # ans = print("product of", n1, "*", n2, "*", n3, "=", prod)
    return(prod)
n1 = int(input("Enter n1 value: "))
n2 = int(input("Enter n2 value: "))
n3 = int(input("Enter n3 value: "))
res = multi(n1,n2,n3)
print("product is:", res)



# Tables
def multi_table(n):
   for i in range (1,13):
    print(i,"x",n,"=",i*n)
n = int(input("which table you want?: "))
multi_table(n)



# Factors of a given number(without arugument,with return value)
def factor(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i)
n = int(input("number?: "))
factor(n)
 


# Find out sum of digits of given in a number, function with argument with return?
def digits(n):
    sum = 0
    while n!=0:
        rem = n%10
        sum = sum+rem
        n = n//10
    return(sum)
n = int(input("Enter the number: "))
res = digits(n)
print("sum of digits in number =", res)


'''# Recusion method'''
    # a fuction which calls itself is called recursive function
    # This concept is called "recusion"
def display():
    n = int(input("Enter the number: "))
    if n==2:
        display()
    else:
        print("over")
display()



# Recursive function
n = int(input("Enter the number: "))
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result = fact(n)
print(result)



n = int(input("Enter the number: "))
a = 0
b = 1
sum = 0
count = 1
while(count<=n):
    print(sum,end="")
    count=+1
    a=b
    b=sum
    sum=a+b
print(sum)