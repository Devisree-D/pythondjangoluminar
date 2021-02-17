from re import *
phone_no=input("enter phone num:")
rule="(91)?\d{10}"
matcher=fullmatch(rule,phone_no)
if matcher==None:
    print("invalid number")
else:
    print("valid number")