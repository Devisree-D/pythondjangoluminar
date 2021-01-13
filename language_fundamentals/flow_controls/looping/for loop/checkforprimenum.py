num=int(input("enter a number: ")) #eg=3
flg=0
if(num==1): #3X
    print("not a prime number")
elif(num==2): #3X
    print("its a prime number")
else:
    for i in range(2,num): #3
        if(num%i==0): #3%2=1 prime number means remainder will not be zero
            flg = flg + 1
            break
        else:  # true
            flg = 0  # flg==0
    if (flg == 0):
        print("prime")
    else:
        print("not prime")