f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    confirmed_cases=int(data[8])
    if state=="Telengana":
        state="Telangana"
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for key,value in dict.items():
    print(key,"===>",value)
result=sorted(dict,key=dict.get,reverse=True)
print(result[0],dict.get(result[0]))
