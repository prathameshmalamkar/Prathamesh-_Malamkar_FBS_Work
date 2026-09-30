
class Laptop:
    def __init__(self,brand,model,ram):
        self.brand = brand
        self.model = model
        self.ram = ram

    def getBrand(self):
        return self.brand
    def setBrand(self,newBrand):
        self.brand=newBrand

    def getModel(self):
        return self.model
    def setModel(self,newModel):
        self.model=newModel

    def getRAM(a):
        return a.ram
    def setRAM(self,newRAM):
        self.ram=newRAM 

    def display(self):
        print(f"Brand ={self.brand},Model ={self.model},RAM ={self.ram}")

l1 = Laptop("HP","AsusVivobook","8 GB")
# l1.display()
print(l1.getRAM())
l1.setRAM("16 GB")
print(l1.getRAM())