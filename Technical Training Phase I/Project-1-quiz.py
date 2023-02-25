'''Quiz Game'''

q1 = """Who won 2011 cricket world cup?
a.Australia
b.India
c.England
d.New Zealand"""
q2 = """Present PM of India ?
a.Narendra Modi
b.Rahul Gandhi
c.MS Dhoni
d.Aravind Kejriwal"""
q3="""10! = ?
a.3628800
b.7286300
c.4293870
d.1472803"""
q4="""Which Indian song is nominated for Oscars 2023?
a.Jaaru mitaayi
b.Naatu Naatu
c.Ma Ma Mahesha
d.Jai Balayya"""
q5="""The value of 5+8*3-8//4*7 is ?
a.10
b.13
c.15
d.17"""
questions={q1:"b",q2:"a",q3:"a",q4:"b",q5:"c"}
name = input("Hi, Whats your name:")
print("Hello",name,"Welcome to the quiz")
score = 0
for i in questions:
    print()
    print(i)
    flag1 = input("Do you want to skip this question?(yes/no)")
    if flag1 == "yes":
        continue
    ans = input("Enter your answer")
    if ans == questions[i]:
        print("Wow ! You scored one point🤩")
        score = score+1
        print("Your current score is",score)
    else:
        print("Wrong answer!You lost one point🤐")
        score = score-1
        print("Your current score is",score)
    print()
    flag2 = input("Do you want to Quit?(yes/no)")
    if flag2 == "yes":
        break

if score>=3:
    print("Your total score is",score,"🥳🥳🥳")
else:
    print("Your total score is",score,"😑😑😑")