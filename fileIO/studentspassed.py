f1=open("students","r")
totstud=[]
for lines in f1:
    totstud.append(lines.rstrip("\n"))
print("total students:",totstud)
f2=open("failedstudents","r")
fail=[]
for lines in f2:
    fail.append(lines.rstrip("\n"))
print("students failed:",fail)
totstud=set(totstud)
fail=set(fail)
passed=totstud.difference(fail)
passed=list(passed)
print("students passed in the exam:",passed)

