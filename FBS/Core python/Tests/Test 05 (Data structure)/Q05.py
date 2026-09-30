
### Q5. Python Program to Find the Union of two Lists without using set concept.

li1=[1,2,3,4,5,6]
li2=[2,3,4,7,8,9]
li3=[]

for i in li1:
    li3.append(i)

for i in li2:
    if(i not in li3):
        li3.append(i)

print(li3)