
class Mechnical:
    def __init__(self):
        print("i am from mech")

    def __str__(self):
        return "mech ka object"

    def getBranch(self):
        print("branch mechnical")

class Electrical:
    def __init__(self):
        print("I am from electrical")

    def __str__(self):
        return "ele ka object"

    def getBranch(self):
        print("ele Branch")

class Mecatronix(Electrical,Mechnical):
    def __init__(self):
        super().__init__()
        print("constructor of mechatronix")

    def __str__(self):
        return super().__str__()+f"\nobj of mechatronix"

    def getBranch(self):
        super().getBranch()
        print("i am from mechatronix")

m1= Mecatronix()
# print(m1)
m1.getBranch()
print(m1)
