f=open("demo","r")
lst=[]
for lines in f:
    words=lines.split(" ")
    for wrd in words:
        lst.append(wrd.rstrip("\n"))
print(lst)

#flatten operation to split word by word
# for lines in f:
#     lst.append(lines.rstrip("\n").split(" "))
# print(lst)
# mywords=[]
# for sub in lst:
#     for wrd in sub:
#         mywords.append(wrd)
# print(mywords)
