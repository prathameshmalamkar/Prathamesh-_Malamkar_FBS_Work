#### 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:

# g. Constructor (Support both parameterized and parameter less)
# h. Destructor
# i. ShowBook


class Shirt:

    # Constructor - supports parameter less and parameterized
    def __init__(self, sid=0, sname="Unknown", type="Unknown",
                 price=0, size="Unknown"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")

    # Display shirt details
    def ShowShirt(self):
        print("Shirt ID :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type :", self.type)
        print("Price :", self.price)
        print("Size :", self.size)


# Parameter less constructor
s1 = Shirt()
s1.ShowShirt()



# Parameterized constructor
s2 = Shirt(101, "Oxford Shirt", "Formal", 1200, "Large")
s2.ShowShirt()
