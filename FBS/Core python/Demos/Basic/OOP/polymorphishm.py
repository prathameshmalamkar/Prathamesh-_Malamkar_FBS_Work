

class Emp():
    def __init__(self,id,name,sal):
        self.id= id
        self.name = name
        self.sal = sal

    def getId(self):
        return self.id 
    def setId(self,newId):
        self.id = newId

    def getName(self):
        return self.name 
    def setName(self,newName):
        self.name = newName

    def getSal(self):
        return self.sal
    def setSal(self,newSal):
        self.sal = newSal
    
    def calSal(self):
        return self.sal

    # def display(self):
    #     print(f"Id ={self.id}, name ={self.name}, sal={self.sal}")

    def __str__(self):
        return f"Id ={self.id}, name={self.name},sal ={self.sal}"
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Hr(Emp):
    def __init__(self, id, name, sal,comm):
        super().__init__(id, name, sal)
        self.comm=comm

    def getcomm(self):
        return self.comm
    def setcomm(self,comm):
        self.comm =comm

    def calSal(self):
        return self.comm +self.sal


    def __str__(self):
        return super().__str__()+f" comm={self.comm}"
  
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Dev(Emp):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getbonus(self):
        return self.bonus
    def setbonus(self,bonus):
        self.bonus=bonus

    def calSal(self):
        return self.bonus + self.sal  #it gives output
    
    # def calSal(self):
    #     return super().calSal()+self.bonus // none+5000 we cannot add
    

    def __str__(self):
        return super().__str__()+f" Bonus={self.bonus}"
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# e1 =Emp(101,"pratham",40000)
h1 =Hr(102,"prem",50000,5000)
d1 =Dev(103,"vansh",35000,4000)

# +++++++++++  Polymorphism  ++++++++++++++++++++++++++++++

# print(e1.calSal())
# print(h1.calSal())
# print(d1.calSal())

# print(e1)
print(h1)
print(d1)
print(d1.calSal())


    