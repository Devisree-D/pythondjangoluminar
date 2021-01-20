lst=[10,8,7,11,12,6,5]
lst.sort()  #5,6,7,8,10,11,12
flg=0
low=0
upp=len(lst)-1
element=int(input("enter element to search:"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg+=1
        break
if flg==0:
    print("element not found")
else:
    print("element found")