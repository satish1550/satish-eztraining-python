name1 = input("Enter the name 1:").lower()
name2 = input("Enter the name 2:").lower()
#If you give spaces in between first and last name
name1 = name1.replace(" ","")
name2 = name2.replace(" ","")
print(name1)
print(name2)
for i in name1:
    for j in name2:
        if i==j:
            name1 = name1.replace(i,"",1)
            name2 = name2.replace(j,"", 1)
            break
count = len(name1+name2)
print(count)
if count>0:
     list1 = ["Friends","Lovers","Affectionate","Marriage","Enemy","Siblings"]
     while len(list1)>1:
         c = count%len(list1)
         s_index = c-1
         if s_index>=0:
             left = list1[:s_index]
             right = list1[s_index+1:]
             list1 = right+left
         else:
             list1 = list1[:len(list1)-1]
     print("Relationship:",list1[0])
else:print("Emter different names")
