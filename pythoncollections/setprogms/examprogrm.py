students=["name1","name2","name3","name3","name4"]
students=set(students)
fail=["name1","name2"]
fail=set(fail)
passed=students.difference(fail)
print("students passed in the exam",passed)


