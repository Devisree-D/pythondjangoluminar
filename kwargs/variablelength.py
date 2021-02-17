#*args in tuple and **kwargs in dict, both can store more than 2 arguments

# def add(*args):
#     return sum(args)
# # or print(add(10,70,20))
# total=add(10,20,30,40,50)
# print(total)

# def print_data(*args):
#     print(args)
# print_data("ajay","luminar","kakkanad")


def print_data(**kwargs):
    print(kwargs)

print_data(name="ajay",company="luminar",place="kakkanad")