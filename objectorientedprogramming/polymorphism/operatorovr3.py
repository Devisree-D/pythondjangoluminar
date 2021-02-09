class Students:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total

    def __str__(self):
            return self.name #to return the string value of the variable

obj=Students(100,"akshay","django",140)
obj1=Students(101,"akhil","mean",140)
obj2=Students(102,"ashil","django",145)

slist=list()
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
total=0

for stud in slist:
    if stud.course=="django":
        total+=stud.total
print(total)