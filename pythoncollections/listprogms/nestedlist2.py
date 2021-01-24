lst=[[10,20],[21,22],[51,52],[53,54,55,56]] #flatten operation
num=[]
for sublst in lst:
    for i in sublst:
        num.append(i)
print(num)
#numlist=[num for numbers in lst for num in numbers]
#print(numlist)