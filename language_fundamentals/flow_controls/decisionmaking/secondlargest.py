num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if(num1<num2)&(num2<num3)|(num3<num2)&(num2<num1):
    print("num2 is second large")
elif(num1==num2):
    print("num1 and num2 are equal")
elif(num2==num3):
    print("num2 and num3 are equal")
elif(num2<num1)&(num1<num3)|(num3<num1)&(num1<num2):
    print("num1 is secondlargest")
elif(num1==num2):
    print("num1 and num2 are same")
elif(num1==num3):
    print("num1 and num3 are equal")
elif(num2<num3)&(num3<num1)|(num1<num3)&(num3<num2):
    print("num3 is second largest")
elif(num3==num1):
    print("num1 and num3 are equal")
elif(num3==num2):
    print("num3 and num2 are equal")