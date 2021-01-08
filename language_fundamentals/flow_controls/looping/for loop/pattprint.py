num=int(input("enter a number:")) #no of rows to print *
for row in range(1,(num+1)): #1....234
    for col in range(0,row): #
        print("*",end="")
    print()