import pickle
class Emp:
    def __init__(self,eid,name,basic):
        self.eid = eid 
        self.name = name 
        self.basic = basic

    def getid(self):
        return self.eid
    def setid(self,eid):
        self.eid = eid

    def getname(self):
        return self.name
    def setname(self,name):
        self.name = name

    def getbasic(self):
        return self.basic
    def setbasic(self,basic):
        self.basic = basic

    def display(self):
        print(self.eid, self.name, self.basic)

    def __str__(self):
        return f"Id:{self.eid}, Name:{self.name}, Basic:{self.basic}"
# __________________________________________________________________________________
def addEmp():
    f =open("emp.dat","ab")
    eid =int(input("enter the id:"))
    ename = input("Enter Employee Name: ") 
    basic = float(input("Enter Basic Salary: ")) 
    e = Emp(eid, ename, basic) 
    pickle.dump(e, f)  # for write code
    # pickle.load(f)# for load or read the data
    f.close() 
    print("Record added successfully.")
# ___________________________________________________________________________________________
def serchEmp():
    id = int(input("enter the id:"))
    f =open("emp.dat","rb")
    found = False
    while True:
        try:
            e =pickle.load(f)
            if e.eid == id:
                e.display()
                found = True
                break
        except Exception:
            break
    f.close()
    if found ==False:
        print("record not found")
# _________________________________________________________________
def deleteEmp():
    id = int(input("Enter employee id to delete: "))

    f = open("emp.dat", "rb")
    records = []
    while True:
        try:
            e = pickle.load(f)
            if e.eid != id:
                records.append(e)

        except EOFError:
            break

    f.close()
    f = open("emp.dat", "wb")
    for e in records:
        pickle.dump(e, f)

    f.close()

    print("Record deleted successfully")
# ___________________________________________________________
def updateEmp():
    id = int(input("Enter employee id to edit: "))
    f = open("emp.dat", "rb")
    records = []
    while True:
        try:
            e = pickle.load(f)
            if e.eid == id:
                e.ename = input("Enter new name: ")
                e.basic = float(input("Enter new salary: "))

            records.append(e)

        except EOFError:
            break

    f.close()

    f = open("emp.dat", "wb")

    for e in records:
        pickle.dump(e, f)

    f.close()

    print("Record updated")
# ________________________________________________-
def displayEmp():
    f = open("emp.dat", "rb")

    while True:
        try:
            e = pickle.load(f)
            e.display()
        except EOFError:
            break

    f.close()



