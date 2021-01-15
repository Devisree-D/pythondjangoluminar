lst=[10,11,12,13,14,15,16,17]
evelst=list()
oddlst=list()
for num in lst:
    if (num%2==0):
        evelst.append(num)
    else:
        oddlst.append(num)
print(evelst)
print(oddlst)
totaleven=sum(evelst)
totalodd=sum(oddlst)
evelst.append(totaleven)
oddlst.append(totalodd)
print(evelst)
print(oddlst)
print("odd sum =",sum(oddlst))
print("even sum =",sum(evelst))
