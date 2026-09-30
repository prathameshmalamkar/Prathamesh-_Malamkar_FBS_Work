
class Book:
    def __init__(self,title,author,lang):
        self.title = title
        self.author = author
        self.lang = lang
        # print("constructor call automatically without creating object")

    def getTitle(self):
        return self.title
    def setTitle(self,newTitle):
        self.title=newTitle

    def getAuthor(self):
        return self.author
    def setAuthor(self,newAuthor):
        self.author=newAuthor

    def getLang(self):
        return self.lang
    def setLang(self,newLang):
        self.lang=newLang


    def display(self):
        print(f"Title ={self.title}, Author ={self.author}, Language ={self.lang}")

b1 =Book("Harry Potter","J.K.Rowling","English")
b2 =Book("Shyam chi Aai","Sane Guruji","Marathi")
b1.display()
# b2.display()

print(b1.getTitle())
b1.setTitle("Atomic Habit")
print(b1.getTitle())
b1.display()  # tittle name is changed Harry potter to Atomic Habit