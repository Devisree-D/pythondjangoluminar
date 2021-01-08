num=int(input("enter a number:"))
res=""
while(num>0):
    data=num%10
    res=res+str(data)
    num=num//10
print(res)