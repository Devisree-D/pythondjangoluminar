lst1=[1,2,3,4,5,6]
lst2=[4,5,6,1,2,3]
for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):

        if lst1[i]==lst2[j]:
            for num in range(j,len(lst2)):
                if num in lst1 :
                    print("rotational")
                    break
                else:
                    print("not rotational")
    break