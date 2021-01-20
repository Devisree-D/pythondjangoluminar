lst=[]
limit=int(input("enter no of elements in the list:"))
for i in range (1,limit+1):
    num=int(input("enter a number:"))
    lst.append(num)
out=list()
total=sum(lst)
for j in lst:
    out.append(total-j)  #20-2, 20-5, .....
print(out)
#no1=int(input("enter num1:"))
#no2=int(input("enter num2:"))
#no3=int(input("enter num3:"))
#lst=[no1,no2,no3]
#a=lst[1]+lst[2]
#b=lst[0]+lst[2]
#c=lst[0]+lst[1]
#out=[a,b,c]
#print(out)