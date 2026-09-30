
class Car:
    def __init__(self,brand,color,no_of_seats):
        self.brand = brand
        self.color = color
        self.seats = no_of_seats

    def getBrand(self):
        return self.brand
    def setBrand(self,newBrand):
        self.brand=newBrand

    def getColor(self):
        return self.color
    def setColor(self,newColor):
        self.color=newColor

    def getSeats(self):
        return self.seats
    def setSeats(self,newSeats):
        self.seats=newSeats

    def display(self):
        print(f"brand ={self.brand},color ={self.color},seats={self.seats}")

c1 =Car("Toyato","black",7)
# c1.display()
print(c1.getBrand())
c1.setBrand("Audi")
print(c1.getBrand())