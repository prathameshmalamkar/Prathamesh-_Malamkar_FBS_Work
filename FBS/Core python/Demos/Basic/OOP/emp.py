class Emp :
    def  ___init___(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    def display (self) :
        print(f"id = {self.id}, name = {self.name}, sal = {self.sal}")
        
e1 =Emp(101, 'pratham', 15000) 
e2 =Emp(102, 'harshal', 15000)
e1.display()  #object
e2.display()  #object