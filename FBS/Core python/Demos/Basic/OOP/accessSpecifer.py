
class Student:
    def __init__(self,id,name):
        self.__id=id
        self.name=name

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id = id 

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name

    def __str__(self):
        return f"Id ={self.__id}\t Name={self.name}"

    def __del__(self):
        print("It is destructer")  
    # A destructor is a special method that is called 
    # when an object is being destroyed or finalized.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MedicalStud(Student):
    def __init__(self, id, name,marks):
        super().__init__(id, name)
        self.marks =marks

    def __str__(self):
        return super().__str__()+f"\tMarks={self.marks}"

s =Student(12,"pratham")
m=MedicalStud(1,"vansh",444)
# print(m)
# print(s)
print(s.__id)
print(m.__id)
print(s.getId())
s.setId(31)
print(s.getId())


# public ( )  It work all over
# protected ( _ ) It work in Hararchay of inheritance
# private ( __ )  it worl with in a class only