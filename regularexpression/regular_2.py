from re import *
#predefined characte set
#pattern="[ab]" # chk for either a or b in lower case
#pattern="[a-z]" #chk for lower case a to z


# pattern="[A-Z]"
# pattern="[a-zA-Z]"
# pattern="[0-9]"
# pattern="[^0-9]" #except for 0 to 9
pattern="[a-zA-Z0-9]"
matcher=finditer(pattern,"abc _7ZK@cgs")
for match in matcher:
    print(match.start())
    print(match.group())