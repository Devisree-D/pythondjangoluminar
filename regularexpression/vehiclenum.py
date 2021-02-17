from re import *
vehicle_num=input("enter a vehicle num:")
rule="kl\d{2}[a-zA-Z]{2}\d{4}"
matcher=fullmatch(rule,vehicle_num)
if matcher==None:
    print("invalid regno")
else:
    print("valid regno")