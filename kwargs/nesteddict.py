employee={
    1000:{"id":1000,"name":"ajay","salary":25000,"exp":1},
    1001:{"id":1001,"name":"tom","salary":30000,"exp":2},
    1002:{"id":1002,"name":"john","salary":35000,"exp":3},
    1003:{"id":1003,"name":"daniel","salary":25000,"exp":4}
}

# def print_employee(id=None,prop=None):
#     if id in employee:
#         print(employee[id][prop])
#
#     else:
#         print("employee does not exits")
# print_employee(id=1000,prop="salary")

# print(employee[1000]) #to print 1st dict of the dict employee
#to print name of employee with id 1001
#if 1001 in employee:
#     print(employee[1001]["name"])
# else:
#     print("employee does not exits")

#salary of 1003
#
# if 1003 in employee:
#     print(employee[1003]["salary"])
# else:
#     print("employee does not exits")

#
def print_employee(**kwargs):
    print(kwargs)
    id = kwargs["id"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass
    else:
        print("employee does not exits")


print_employee(id=1000,prop="exp")



# def print_employee(id=None):
#     if id in employee:
#         print(employee[id]["name"])
#     else:
#         print("employee with this id does not exits")
# print_employee(id=1000)