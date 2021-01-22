f=open("demo","r")
dict={}
lst=[]
for lines in f:
    words=lines.split(" ") #this is , a demo  , text file
    for wrd in words: # this, is , demo
        lst.append(wrd.rstrip("\n"))
#print(lst)
for i in lst:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
#for key,value in dict.items():
    #print(key,",",value)
result=sorted(dict,key=dict.get,reverse=True)
print(result[0])



