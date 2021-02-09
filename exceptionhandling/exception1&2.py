lst = [10, 20, 30]
pos = int(input("enter the position to print element:"))
num1=int(input("enter a num1"))
num2=int(input("enter a num2"))
try:
    res=num1/num2
    print("res=",res) #once exception occured it will move to except
    print(lst[pos])
except Exception as e:
    print(e.args)