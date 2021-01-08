num1=int(input("enter no1:"))
num2=int(input("enter no2:"))
num3=int(input("enter no3:"))
if(num1>num2)&(num1>num3):
    print("number1 is largest")
elif(num2>num1)&(num2>num3):
    print("number2 is largest")
elif(num3>num1)&(num3>num2):
    print("number3 is largest")
elif(num1==num2)&(num2==num3):
    print("all 3 are equal")
elif(num1==num2):
    print("num1 and num2 are largest")
elif(num2==num3):
    print("num2 and num3 are largest")
elif(num3==num1):
    print("num3 and num1 are largest")