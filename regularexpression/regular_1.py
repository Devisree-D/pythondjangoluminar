from re import *
pattern="ab"
matcher=finditer(pattern,"ababababbbbbbbaaaaaaba")
#                          0 1 2 3 4 5 6 7 8 9 10
cnt=0

for match in matcher:
    print(match.start()) #position match occured
    print(match.group()) #which object match occured
    cnt+=1
print(cnt) #to find the no of matches