#nested loop
for row in range(1,5):
    for col in range(1,8):
        sum=row+col
        diff=col-row
        if(row==4)|(sum==5)|(diff==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
