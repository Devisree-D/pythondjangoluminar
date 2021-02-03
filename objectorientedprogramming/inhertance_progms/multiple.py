class Parent:
    def m1(self):
        print("inside parent")
class Child:
    def m1(self):
        print("inside child")
class Subchild(Parent,Child): #it can be parent child or child parent, inheritance takesplace in this order

    def m3(self):
        print("inside sub child")
obj=Subchild()
obj.m3()

obj.m1()