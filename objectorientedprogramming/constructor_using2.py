class Stud:
    def __init__(self):
        print("no arg constructor")
    def __init__(self,name,age):
        print("two argument constructor")

obj=Stud()
obj=Stud("ajay",12) #recently implemented constructor will only work
