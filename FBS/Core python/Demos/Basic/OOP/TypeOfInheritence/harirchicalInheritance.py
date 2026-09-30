
class Emp:
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

    def __str__(self):
        return f"Id ={self.id}\nname={self.name}\nsal ={self.sal}"
    
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
        return super().__str__()+f"\ncomm={self.comm}"
  
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
        return self.bonus + self.sal

    def __str__(self):
        return super().__str__()+f"\nBonus={self.bonus}"
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class JrHr(Hr):
    def __init__(self, id, name, sal, comm,yrExp):
        super().__init__(id, name, sal, comm)
        self.yrExp=yrExp

    def getyrExp(self):
        return self.yrExp
    def setyrExp(self,yrExp):
        self.yrExp=yrExp

    def __str__(self):
        return super().__str__()+f"\nYearOfExperience ={self.yrExp}"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class SrHr(Hr):
    def __init__(self, id, name, sal, comm,yrExp):
        super().__init__(id, name, sal, comm)
        self.yrExp=yrExp

    def getyrExp(self):
        return self.yrExp
    def setyrExp(self,yrExp):
        self.yrExp=yrExp

    def __str__(self):
        return super().__str__()+f"\nYearOfExperience={self.yrExp}"
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class JrDev(Dev):
    def __init__(self, id, name, sal, bonus,yrExp):
        super().__init__(id, name, sal, bonus)
        self.yrExp=yrExp

    def getyrExp(self):
        return self.yrExp
    def setyrExp(self,yrExp):
        self.yrExp=yrExp

    def __str__(self):
        return super().__str__()+f"\nYearOfExperience={self.yrExp}"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class SrDev(Dev):
    def __init__(self, id, name, sal, bonus,yrExp):
        super().__init__(id, name, sal, bonus)
        self.yrExp=yrExp

    def getyrExp(self):
        return self.yrExp
    def setyrExp(self,yrExp):
        self.yrExp=yrExp

    def __str__(self):
        return super().__str__()+f"\nYearOfExperience={self.yrExp}"

    

h1 =JrHr(102,"pratham",40000,5000,1)
h2 =SrHr(101,"harshal",50000,10000,5)
d1=JrDev(103,"Vansh",35000,5000,2)
d1=SrDev(104,"prem",50000,10000,7)
print(h1)
print(h2)
print(d1)




