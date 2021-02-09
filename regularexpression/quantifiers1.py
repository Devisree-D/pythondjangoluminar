from re import *

# pattern="a+" #any no of a excluding 0 no of a
# pattern="a*" #any nof a including 0 num of a

# pattern="a?" #single num of a including 0 num of a

# pattern="a{2}" #2 a as a set
pattern="a{2,4}" #2 to 4 num of a
matcher=finditer(pattern,"aaabaaaaabababbbbbbbaaaaaaba")
for match in matcher:
    print(match.start(),"-->",match.group()) #position match occured
