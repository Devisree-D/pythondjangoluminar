lst=[1,2,3,4,5]
n=int(input("enter a number:"))
for i in range (0,len(lst)): #0
    for j in range (i+1,len(lst)):  #1
        if((lst[i]+lst[j])==n): #1+2=3
            print(lst[i],lst[j])