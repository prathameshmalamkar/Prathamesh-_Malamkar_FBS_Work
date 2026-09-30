class Vehicle:
    
    def __init__(self, wheels, person):
        self.wheels = wheels
        self.person = person

    def getWheel(self):
        return self.wheels

    def setWheel(self, wheels):
        self.wheels = wheels

    def getPerson(self):
        return self.person

    def setPerson(self, person):
        self.person = person

    def calculateToll(self, persons):
        pass


class TwoWheeler(Vehicle):

    def calculateToll(self, persons):
        toll = 20

        if persons > 2:
            toll = toll + (persons - 2) * 10

        return toll


class ThreeWheeler(Vehicle):

    def calculateToll(self, persons):
        toll = 30

        if persons > 3:
            toll = toll + (persons - 3) * 20

        return toll


class FourWheeler(Vehicle):

    def calculateToll(self, persons):
        toll = 40

        if persons > 4:
            toll = toll + (persons - 4) * 40

        return toll


class HeavyVehicle(Vehicle):

    def calculateToll(self, persons):
        toll = 60

        if persons > 6:
            toll = toll + (persons - 6) * 100

        return toll


def main():

    person = int(input("Enter the no of persons: "))

    v = TwoWheeler(2, person)
    print("Two Wheeler Toll =", v.calculateToll(person))

    v = ThreeWheeler(3, person)
    print("Three Wheeler Toll =", v.calculateToll(person))

    v = FourWheeler(4, person)
    print("Four Wheeler Toll =", v.calculateToll(person))

    v = HeavyVehicle(6, person)
    print("Heavy Vehicle Toll =", v.calculateToll(person))


main()