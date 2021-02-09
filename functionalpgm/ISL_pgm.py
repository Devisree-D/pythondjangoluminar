from functools import reduce

isl=[{"team":"mumbai city","MP":16,"win":10,"draw":4,"loss":2,"gf":25,"ga":11,"gd":14,"points":34},
    {"team":"ATK","MP":15,"win":9,"draw":3,"loss":3,"gf":20,"ga":10,"gd":10,"points":30},
    {"team":"goa","MP":16,"win":5,"draw":8,"loss":3,"gf":24,"ga":19,"gd":5,"points":23},
    {"team":"hyderabad","MP":16,"win":5,"draw":8,"loss":3,"gf":20,"ga":16,"gd":4,"points":23},
    {"team":"northeast","MP":16,"win":5,"draw":8,"loss":3,"gf":21,"ga":20,"gd":1,"points":23},
    {"team":"bengaluru","MP":16,"win":4,"draw":7,"loss":5,"gf":19,"ga":19,"gd":0,"points":19},
    {"team":"jamshedpur","MP":16,"win":4,"draw":6,"loss":6,"gf":15,"ga":19,"gd":-4,"points":18},
    {"team":"chennai","MP":16,"win":3,"draw":8,"loss":5,"gf":11,"ga":16,"gd":-5,"points":17},
    {"team":"east bengal","MP":16,"win":3,"draw":7,"loss":6,"gf":14,"ga":21,"gd":-7,"points":16},
    {"team":"Kerala blasters","MP":16,"win":3,"draw":6,"loss":7,"gf":20,"ga":27,"gd":-7,"points":15},
    {"team":"odisha","MP":15,"win":1,"draw":5,"loss":9,"gf":14,"ga":25,"gd":-11,"points":8},
]


point_high=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["points"],isl))),isl))
print(point_high)
point_low=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["points"],isl))),isl))
print(point_low)

# points=[]
# goals_for=[]
# for team in isl:
#     points.append(team["points"])
# print(points)
#
# highpts=reduce(lambda num1,num2:num1 if num1>num2 else num2,points)
# print(highpts)
#
# lowpts=reduce(lambda num1,num2:num1 if num1<num2 else num2,points)
# print(lowpts)

# for team in isl:
#     goals_for.append(team["gf"])
# print(goals_for)
#
# gfhigh=reduce(lambda num1,num2:num1 if num1>num2 else num2,goals_for)
# print(gfhigh)