class Maths:
    def add(self):
        print("inside no arg")
    def add(self,num1):
        print("inside one arg")
    def add(self,num1,num2):
        print("inside 2 arg")

obj=Maths()
obj.add(1,2) #only the recently given  method works