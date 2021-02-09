# [1,2,3,4]  [2,4,5,6,8]
from functools import reduce
lst1=[1,2,3,4]
lst2=[2,4,5,6,8]

lst=reduce(lambda num1,num2:num1 if num1==num2 else num2,list(map(lambda num)))
print(lst)