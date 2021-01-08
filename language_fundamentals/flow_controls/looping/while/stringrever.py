name="luminar"
length=len(name)-1 #0to6
reverse=""
while(length>=0):
    reverse+=name[length]
    length-=1
print(reverse)