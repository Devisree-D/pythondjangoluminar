f=open("demo","r")
dict={}
for lines in f:
    words=lines.split(" ") #this is , a demo  , text file
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
for key,value in dict.items():
    print(key,",",value)
result=sorted(dict,key=dict.get,reverse=True)
print(result[0])




