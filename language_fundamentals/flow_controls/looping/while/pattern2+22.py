num=input("enter a number ") # enter any number, it is taken as string eg:3
data=0 #initialize a variable
i=1 #initialize i
pattern=""
while(i<=int(num)): #from 1 to that input number eg:1,2,3
    res=num*i #3*1=3............3*2=33.........3*3=333
    pattern=pattern+"+"+res
    data=data+int(res) #0+3=3...3+33=36.........36+333=369
    i+=1 #......2.....3........4
pattern=pattern.lstrip("+")
print(pattern,"=",data)
