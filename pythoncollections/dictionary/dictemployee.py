employee={"id":100,"ename":"ajay","salary":30000}
if("salary" in employee):
    print("salary exist")
else:
    print("salary doesnot exist")

if(employee["salary"]<35000):
    employee["salary"]+=3000
print(employee)
