for row in range(1,5): #1
    for col in range(1,row+1): #otherwise (0,row)
        print(col,end="") #or col+1
    print()
#1
#12
#123
#1234