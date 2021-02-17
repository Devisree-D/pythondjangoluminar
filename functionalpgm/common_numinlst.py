# [1,2,3,4]  [2,4,5,6,8]

lst1=[1,2,3,4]
lst2=[2,4,5,6,8]

lst=list(filter(lambda num:num in set(lst1),set(lst2)))
print(lst)