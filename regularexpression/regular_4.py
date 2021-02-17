#first chara a to k
#sec must be a mul of 3
#followed by any no of chara
from re import *
var_name=input("enter a variable name:")
rule="[a-k][369][a-zA-Z0-9]*"
matcher=fullmatch(rule,var_name)
if matcher==None:
    print("invalid variable name")
else:
    print("valid variable")