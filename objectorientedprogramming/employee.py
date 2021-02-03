class Employee:
    def set_employee(self,empid,name,designation,salary):
        self.empid=empid
        self.name=name
        self.designation=designation
        self.salary=salary

    def get_employee(self):
        print("name=",self.name)
        print("emp id=",self.empid)
        print("designation=",self.designation)
        print("salary=",self.salary)

obj1=Employee()
obj1.set_employee(1001,"alex","developer",25000) #if constructor created, then step can be skipped

obj1.get_employee()

obj2=Employee()
obj2.set_employee(1002,"john","data analyst",20000)
obj2.get_employee()