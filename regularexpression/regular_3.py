from re import *
#chk for predefined character


# pattern="\s" #chk for space
# pattern="\d" #chk for digit
#
# pattern="\D" #except digit
#pattern="\w" # chk for all words except for spcl chara
pattern="\W" #except words
matcher=finditer(pattern,"abc _7ZK@cgs")
for match in matcher:
    print(match.start(),"-->",match.group())
