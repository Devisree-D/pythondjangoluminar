from re import *
f=open("vehiclereg_num.txt","r")
for lines in f:
    regnum=lines.rstrip("\n").split(",")


    for num in regnum:
        rule="kl[\d]{2}[a-zA-Z]{2}[\d]{4}"
        matcher=fullmatch(rule,num)
        if matcher==None:
            print(num,"--->","invaild vehicle number")
        else:
            print(num,"--->","valid vehicle number")