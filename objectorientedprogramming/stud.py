class Employee:
    def __init__(self, empid, name, designation, salary):
        self.empid = empid
        self.name = name
        self.designation = designation
        self.salary = salary

    def print_emp(self):
        print(self.empid,self.name,self.designation,self.salary)
obj=Employee(100,"ajay","ba",10000)
obj.print_emp()
