from re import *
email=input("enter emailid:")
rule="[a-zA-Z.]*[\d]*@gmail.com"
matcher=fullmatch(rule,email)
if matcher==None:
    print("invalid mailid")
else:
    print("valid mailid")