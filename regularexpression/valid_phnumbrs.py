from re import *
f=open("phnumbers","r")
for lines in f:
    phnum=lines.rstrip("\n").split(",")


    for num in phnum:
        rule="(91)?[\d]{10}"
        matcher=fullmatch(rule,num)
        if matcher==None:
            print(num,"--->","invaild phone number")
        else:
            print(num,"--->","valid phone number")