# Python Assignment – (Pickling and Unpickling)
# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

# pickling = python object store into file 
# unpickling = file convert into python object 

import emp

while True:
    print("\n Employee details")
    print(" 1.Add records")
    print(" 2.Search records")
    print(" 3.Delete records")
    print(" 4.Update records")
    print(" 5.Display records")
    print(" 6. Exit ")

    ch =int(input("enter your choice:"))
    if ch == 1:
        emp.addEmp()
    elif ch ==2:
        emp.serchEmp()
    elif ch == 3:
        emp.deleteEmp()
    elif ch ==4:
        emp.updateEmp()
    elif ch ==5:
        emp.displayEmp()
    elif ch ==6:
        print("Thank Youuu....")
        break
    else:
        print("Invalid choice")