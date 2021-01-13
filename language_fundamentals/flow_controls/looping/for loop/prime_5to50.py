low=int(input("enter lower limit:"))
upp=int(input("enter upper limit:"))
for num in range(low,(upp+1)):
    flg=0
    for i in range(2,num):
        if(num%i==0):
            flg=flg+1
            break
        else:
            flg=0
    if(flg==0):
        print(num,end=",")


