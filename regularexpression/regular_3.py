from re import *
#chk for predefined character


# pattern="\s" #chk for space
# pattern="\d" #chk for digit
#
# pattern="\D" #except digit
pattern="\w" # chk for all chara except for spcl chara &space
# pattern="\W" #include spcl char &space except words&num
matcher=finditer(pattern,"abc _7ZK@cgs")
for match in matcher:
    print(match.start(),"-->",match.group())
