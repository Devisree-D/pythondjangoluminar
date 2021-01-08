num=int(input("enter the number to reverse:"))#123
while(num>0): #until num equals 0
    temp=num%10 #123%10=3.....12%10=2.....1%10=1
    num=num//10 #123//10=12......12//10=1....1//10=0
    print(temp,end=" ") #3,2,1
