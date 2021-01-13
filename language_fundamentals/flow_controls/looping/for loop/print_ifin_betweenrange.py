num=int(input("enter a number:"))
low=int(input("enter lower limit:"))
upp=int(input("enter upper limit:"))
for i in range(1,(upp+1)):
        data=i**num
        if(data>=low)&(data<upp):
            print(i,end=",")
