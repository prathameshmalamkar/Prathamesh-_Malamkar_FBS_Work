### Q02. Create a class Distance with data members as km,m and cm and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    def __init__(self, km, m):
        self.km = km
        self.m = m
        self.total_m = (km * 1000) + m

    # Destructor
    def __del__(self):
        print("Distance object destroyed")

    # Operator overloading +
    def __add__(self, other):

        total = self.total_m + other.total_m

        km = total // 1000
        m = total % 1000

        return Distance(km, m)

    # Operator overloading -
    def __sub__(self, other):

        total = self.total_m - other.total_m

        km = total // 1000
        m = total % 1000

        return Distance(km, m)

    # Display
    def __str__(self):
        return f"{self.km} km {self.m} m"


# Creating objects
d1 = Distance(10, 500)
d2 = Distance(5, 750)

print("Distance 1:", d1)
print("Distance 2:", d2)

# Addition
d3 = d1 + d2
print("Addition:", d3)

# Subtraction
d4 = d1 - d2
print("Subtraction:", d4)