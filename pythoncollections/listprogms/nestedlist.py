students=[
    [10,"ajay","bca",250],
    [11,"vjay","bca",240],
    [12,"sibin","bca",220],
    [13,"dino","mca",220],
    [14,"tom","mca",180],
    [15,"jain","mca",250],
]

#total of bca and mca separate
btotal, mtotal =0,0
for stud in students:
    if stud[2]=="bca":
        btotal=btotal+stud[3]
    elif(stud[2]=="mca"):
        mtotal=mtotal+stud[3]
print("total bca =",btotal)
print("total mca =",mtotal)



#sum of total marks
#marks=0
#for stud in students:
    #marks=marks+stud[3]
#print("total =",marks)


#students who have marks above 240
#for stud in students:
    #if stud[3]>240:
        #print(stud[1])