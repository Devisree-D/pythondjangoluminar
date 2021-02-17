from re import *
f=open("emailid.txt","r")
for lines in f:
    emailid=lines.rstrip("\n").split(",")


    for id in emailid:
        rule="[\w._!#$%^&*+-/=?^'|{]+@gmail.com"
        matcher=fullmatch(rule,id)
        if matcher==None:
            print(id,"--->","invaild email id")
        else:
            print(id,"--->","valid email id ")