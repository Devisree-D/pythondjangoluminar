f=open("movies.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
#print(words)
    year=words[2]
    if year not in dict:
        dict[year]=1
    else:
        dict[year]+=1

for key,value in dict.items():
    print(key,"===>",value)
res=sorted(dict)
print(res)
data=sorted(dict,key=dict.get,reverse=True)
print(data[0],dict.get(data[0]))

