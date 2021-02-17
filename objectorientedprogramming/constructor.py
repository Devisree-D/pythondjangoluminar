class Student:
    def __init__(self, roll,course, name):
        self.roll = roll
        self.course=course
        self.name = name

    def get_student(self):
        print("name=", self.name)
        print("roll=", self.roll)
        print("course=",self.course)


obj = Student(1001,"django","akhil") #constructor invoked
obj.get_student()
print(obj.course)
print(obj.roll)