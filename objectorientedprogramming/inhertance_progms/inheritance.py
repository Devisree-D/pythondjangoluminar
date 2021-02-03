class Parent: #class Parent(object) by default there is "object" is the parent class for each parent
    def phone(self):
        print("i have nokia 5310")
class Child(Parent):
    pass

c=Child()
#print(type(c)) #print(c)--while printing an object __str__() will invoke object//inheritance and method overriding
c.phone()