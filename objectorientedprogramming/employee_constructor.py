class Employee:
    def __init__(self,empid,name,designation):
        self.empid=empid
        self.name=name
        self.designation=designation

    def get_employee(self):
        print("name=",self.name)
        print("emp id=",self.empid)
        print("designation=",self.designation)

obj=Employee(1001,"alex","ba")
obj.get_employee()