employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",25000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],

]
#developer with least salary
d_salarylist=[]
for emp in employees:
    if emp[2]=="developer":
        d_salarylist.append(emp[3])
low_salary=min(d_salarylist)
print(low_salary)



#for emp in employees:
    #salary_list.append(emp[3])
#high_salary=max(salary_list)
#print(high_salary)



#no_of_employees = len(employees)
#print("no_of_employees =",no_of_employees)




#print how much salary compny should raise
#total =0
#for emp in employees:
    #total=total+emp[3]
#print("total salary =", total)




#group designations
#count_ba,count_dataanalyst,count_developer=0,0,0
#for emp in employees:
    #if emp[2]=="developer":
        #count_developer+=1
    #elif emp[2]=="dataanalyst":
        #count_dataanalyst+=1
    #elif emp[2]=="ba":
        #count_ba+=1
#print("ba",count_ba,"dataanalyst",count_dataanalyst,"developer",count_developer)
