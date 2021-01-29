f=open("students","r")
students={}
for lines in f:
   id,name,total,course=lines.rstrip("\n").split(",")
   if id not in students:
       students[id]={"id":id,"name":name,"total":total,"course":course}
print(students)
def print_data(**kwargs):
    print(kwargs)
    id=kwargs["id"]
    if id in students:
        print(students[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(students[id][prop])
        else:
            pass
    else:
        print("student with this roll num does not exists")
print_data(id="1000",prop="course")
