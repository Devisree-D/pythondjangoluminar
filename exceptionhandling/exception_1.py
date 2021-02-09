num1=int(input("enter a num1"))
num2=int(input("enter a num2"))
try:
    res=num1/num2
    print("res=",res)
except Exception as e:
    print("exception occured")
print("i have one database transaction")
print("i have file operation")