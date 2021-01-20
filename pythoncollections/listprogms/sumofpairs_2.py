lst=[1,2,3,4,5]
num=int(input("enter the number: "))
low=0
upp=len(lst)-1 #4
pairs=[]
while(low<upp): #0<4.....1<4
    ele=lst[low]+lst[upp] #1+5=6......7
    if(num==ele):
        pairs.append((lst[low],lst[upp]))
        upp-=1
    elif(num>ele):
        low+=1
    else:
         upp-= 1
print(pairs)

