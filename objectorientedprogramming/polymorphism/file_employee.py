class Employee:
    def __init__(self,empid,name,desig,exp,salary):
        self.empid=empid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.name


f=open("employee.txt","r")
emplist=[]
sallist=[]

for lines in f:
    empid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(Employee(empid,name,desig,exp,salary))
    sallist.append(salary)


#no of emp as developer
# cnt=0
# for employee in emplist:
#     if employee.desig=="developer":
#         cnt+=1
# print(cnt)
#######using funct####
# cnt=len(list(filter(lambda employee:employee.desig=="developer",emplist)))
# print(cnt)



#desig as developer
# for employee in emplist:
#     if employee.desig=="developer":
#         print(employee)
#######using funct######
# develop=list(filter(lambda employee: employee.desig=="developer",emplist))
# for emp in develop:
#     print(emp)

# highsal=max(sallist)
#
# for employee in emplist:
#     if employee.salary==highsal:
#         print(employee,employee.salary)
#######using funct######
# hig=max(list(map(lambda employee:employee.salary,emplist)))
# print(hig)

# lowsal=min(sallist)
# for employee in emplist:
#     if employee.salary==lowsal:
#         print(employee,employee.salary)