
class Account:
    def __init__(self,acName,bal):
        self.acName=acName
        self.bal = bal

    def getAcName(self):
        return self.acName
    def setAcName(self,acName):
        self.acName= acName

    def getBal(self):
        return self.bal
    def setBal(self,bal):
        self.bal= bal

    # def deposite(self,amount):
    #     self.bal += amount
    #     print("amount deposited:",amount)

    def __str__(self):
        return f"Account Holder:{self.acName}\nBalance:{self.bal}"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class SavingAccount(Account):
    def __init__(self, acName, bal,inRate):
        super().__init__(acName, bal)
        self.inrate = inRate

    def getinRate(self):
        return self.inrate
    def setinRate(self,inRate):
        self.inrate= inRate

    def __str__(self):
        return super().__str__()+f"\nInterest Rate ={self.inrate}"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class StudSavingAcc(SavingAccount):
    def __init__(self, acName, bal, inRate,stuId):
        super().__init__(acName, bal, inRate)
        self.id = stuId

    def getId(self):
        return self.id
    def setId(self,stuId):
        self.id = stuId

    def __str__(self):
        return super().__str__()+f"\nStudent Id ={self.id}"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

a1=SavingAccount("pratham",1000,"5%")
print(a1)
print("-------------------------------------------")
a2=StudSavingAcc("prem",2000,"5%",101)
print(a2)



