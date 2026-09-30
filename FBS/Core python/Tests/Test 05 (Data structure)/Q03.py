
### Q3. A list contains sublist with Emp information as follows :
# Data = [[101,”pratham”,45000],[340,”Raj”,13000],
# [210,”rohan”,14000],[320,”Suresh”,35000]]
# Write a program to sort the list based on salary.

Data = [[101,"pratham",45000],[340,"Raj",13000],
[210,"rohan",14000],[320,"Suresh",35000]]

def sort(li):
    for i in range(len(li)):
        for j in range(len(li) -i -1):
            if(li[j][2] >li[j+1][2]):
                li[j],li[j+1] = li[j+1],li[j]
print(f"Before Swaping\n {Data} ")
sort(Data)
print(f"After Swaping \n{Data}")
