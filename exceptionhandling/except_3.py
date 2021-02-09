num1=int(input("enter a num1"))
num2=int(input("enter a num2"))
try:
    res=num1/num2
    print(res)
except:
    num2=int(input("enter num2:"))
    try:
        res = num1 / num2
        print(res)
    except Exception as e:
        print(e.args)
        num2 = int(input("enter num2:"))
        res = num1 / num2
        print(res)

finally:
    print("i have one database")
    print("i have file operation")

