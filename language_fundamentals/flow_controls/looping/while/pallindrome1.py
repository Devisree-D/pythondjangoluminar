num=int(input("enter the number to print reverse:"))#123#store num to temp....(123,12,1,0)
result=0
while (num>0): #until num equals  or less than 0
    temp=num%10 #123%10=3..............12%10=2.......1%10=1
    result=10*result+temp#10*0+3=3....10*3+2=32.....10*32+1=321
    num=num//10 #123//10=12............12//10=1......1//10=0
print("result=",result) #3,2,1
