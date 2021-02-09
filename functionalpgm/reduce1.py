from functools import reduce
lst=[10,11,12,13,14,15]
# sum=reduce(lambda num1,num2:num1+num2,lst)
# print(sum)
high=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(high)

low=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(low)