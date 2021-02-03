class Parent:
    def mobile(self):
        print("nokia 5310")
class Child(Parent):
    def mobile(self):
        print("iphone 12")
obj=Child()
obj.mobile()