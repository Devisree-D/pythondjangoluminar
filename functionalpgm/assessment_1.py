from functools import reduce
employees=[
            {"empid":10,"name":"christy","desig":"dataanalyst","sal":50000,"join":1985,"resign":1990},
            {"empid":11,"name":"jhon","desig":"ba","sal":25000,"join":1989,"resign":1990},
            {"empid":12,"name":"sab","desig":"dataanalyst","sal":40000,"join":1982,"resign":1995},
            {"empid":13,"name":"tom","desig":"developer","sal":40000,"join":1980,"resign":1995},
            {"empid":14,"name":"jhoni","desig":"developer","sal":30000,"join":1984,"resign":1996},
            {"empid":15,"name":"sabir","desig":"dataanalyst","sal":50000,"join":1985,"resign":1997},
            {"empid":16,"name":"tino","desig":"developer","sal":40000,"join":1983,"resign":1994},
            {"empid":17,"name":"tomis","desig":"developer","sal":47000,"join":1981,"resign":1999},
            {"empid":18,"name":"jhonis","desig":"developer","sal":32000,"join":1989,"resign":1995},
]
# salary=[]
# for emp in employees:
#     salary.append(emp["sal"])
#
#
# print(max(salary))

#salary=list(filter(lambda emp:emp["sal"]==reduce(lambda num1,num2:num1 if num1>num2 else num2,list(map(lambda emp:emp["sal"],employees))),employees))
salary=reduce(lambda num1,num2:num1 if num1>num2 else num2,(list(map(lambda emp:emp["sal"],employees))))
print(salary)
