
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
        return f"Account Holder:{self.acName},Balance:{self.bal}"

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
a1=SavingAccount("pratham",1000,"5%")
print(a1)

        