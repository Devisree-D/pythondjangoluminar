pattern="ABCABBAAEEEEEEDD"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)

data=sorted(dict,key=dict.get,reverse=True) #key=dict.get --to get acsending order
print(data[0])
