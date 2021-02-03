class Person:
    def setPerson(self,age,name):
        self.age=age
        self.name=name
    def printPerson(self):
        print("name=",self.name)
        print("age=",self.age)

obj=Person()
obj.setPerson(25,"ajay")
obj.printPerson()

obj1=Person()
obj1.setPerson(24,"jack")
obj1.printPerson()