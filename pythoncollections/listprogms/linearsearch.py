lst=[10,11,12,13,14,15]
element=int(input("enter element u want to search:"))
flg=0
cnt=1
for num in lst:
    if(element==num):
        flg+=1
        break
        cnt+=1
    else:
        pass
if flg==0:
    print("element not found")
else:
    print("element found",cnt)