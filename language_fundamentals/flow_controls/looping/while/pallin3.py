num=int(input("enter the number to check pallindrome:"))#123#store num to temp....(123,12,1,0)
digit=num
result=0
while (num>0): #until num equals  or less than 0
    temp=num%10 #123%10=3..............12%10=2.......1%10=1
    result=10*result+temp#10*0+3=3....10*3+2=32.....10*32+1=321
    num=num//10 #123//10=12............12//10=1......1//10=0
if(result==digit):
    print("the number is pallindrome")
else:
    print("the number is not pallindrome")