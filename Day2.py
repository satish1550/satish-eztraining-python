# DAY 2

# Bitwase Oprators
    # 0's and and 1's
    # Some oprations if you do like dz t will faster
    # Like - Compressing Data
    # sending Data in network to network

print(12&4)
print(12|4)
print(~12)
print(3&4, 3|4, ~3,~4,~14, ~0, ~(-12))
print(2<<3)
print(2>>3)
print(2^3)


# get any two number both no. should be lessthan or equal to 15 perform &, | and ~. ?
n1, n2 = int(input("Enter n1 value: ")), int(input("Enter n2 value: "))
print(n1&n2)
print(n1|n2)
print(n1^n2)


# Taking multiple inputs!!
n=int(input("Enter Size: "))
l=list(map(str,input("Enter Data: ").split()))[0:1:n]
print(l)


# Find product of ten integers?
n = 10
product =1
l = list(map(int, input("Enter 10 Numbers: ").split()))
for i in l:
    product = product*i
print(product)


print("it's", "a", "good", "day",end=" **|** ", sep="##")
print("all", "is", "good")


# Fillied upside down Triangle:
print("*******")
print(" ***** ")
print("  ***  ")
print("   *   ")


# Hallow Hart:
print("    * *    * *     ")
print("  *      *      *  ")
print("  *             *  ")
print("   *           *   ")
print("     *       *     ")
print("       *   *       ")
print("         *         ")


# Get a number as input and find out wether it is a 500 or not?
Num1 = int(input('Enter any number: '))
if (Num1 == 500):
    print("Your value is ", Num1)
else:
    print("Your value is is", Num1, "not 500..")


# Check given no. is "Even-Positive" or "Odd-Positive" "Even-Negative" or "Odd-Negative"?
Num1 = int(input("Enter any number: "))
if(Num1%2==0):
    if(Num1>0):
        print("You enter an 'Even-Positive' Number")
    else:
        print("You enter an 'Even-Negative' Number")
elif(Num1>0):
    print("You enter an 'Odd-Positive' Number")
else:
    print("You enter an 'Odd-Negative' Number")


# Get two no. as input and find out bigger one?
n1,n2 = int(input("Enter n1 value: ")), int(input("Enter n2 value: "))
if(n1>n2):
    print(n1,"is larger than",n2)
else:
    print(n2,"is larger than",n1)


# Check given no. is Float or Integer?
number = input("")
n= 10.0
res = n-int(n)
if(res>0 or res!=0):
    print("Float")
else:
    print("Int")


# Get three no. as input and find out gratest no. among those no.?
n1, n2, n3 = int(input("Enter n1 value: ")), int(input("Enter n2 value: ")), int(input("Enter n3 value: "))
if (n1 > n2):
    if (n1 > n3):
        print(n1, 'is greater than', n2, "and", n3)
    else:
        print(n3, 'is greater than', n1, "and", n2)
elif (n1 < n2):
    if (n1 > n3):
        print(n1, 'is greater than', n2, "and", n3)
    else:
        print(n3, 'is greater than', n1, "and", n2)

else:
    print(n2, 'is greater than', n1, "and", n3)


# Check given no. is divisible by 11 or not?
n = int(input("Enter n value: "))
if (n % 11 == 0):
    print(n, "is divisible by 11.")
else:
    print(n, "is not divisible by 11.")


# Check given no. is divisible by both 2 and 5?
# Model 1:
n = int(input("Enter n value: "))
if (n % 5==0 and n %2==0):
    print(n, "is divisible by both 2 and 5.")
else:
    print(n, "is not divisible by both 2 and 5.")

# Model 2:
n = int(input("Enter n value: "))
if (n % 5 == 0):
    if(n % 2 == 0):
        print(n, "is divisible by both 2 and 5.")
    else:
        print(n, "is divisible by only 5.")
elif(n % 2 == 0):
    print(n, "is divisible by only 2.")
else:
    print(n, "is not divisible bt 5.")

# Weahter conditions:
t = int(input('Enter temp: '))
if (t >= 45):
    print("Hottest")
elif (t <= 45 and t >= 40):
    print("Hot")
elif (t <= 40 and t >= 25):
    print("Moderatre")
elif (t <= 25 and t >= 10):
    print("Cold")
else:
    print("Chill")


'''# while'''
n = 100
i = 0
while i<=n:
    print(i)
    i =i+1


''' Number Game'''
import random
number = random.randrange(1, 50)
guess = int(input("Enter Number: "))

while (number != guess):
    if (guess < number):
        print("Too Low")
        guess = int(input("Enter Number: "))
    elif (guess > number):
        print("Too High")
        guess = int(input("Enter Number: "))
    else:
        break
    print("Ha Ha Ha you got it")