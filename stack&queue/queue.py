size=int(input("enter the size of queue:"))
q=[]
rear=0
front=0
n=1
def insertion():
    item=int(input("enter item:"))
    global rear
    if rear<size:
        q.insert(rear,item)
        print(rear)
        rear+=1
    else:
        print("queue full")
def deletion():
    global front
    global rear
    if front<size & rear>0:
        print(q[front],"out from queue")
        front+=1
    else:
        print("queue empty")


while(n!=0):
    option=int(input("enter operation press 1)insertion 2)deletion:"))
    if option==1:
        insertion()
    elif option==2:
        deletion()

    n=int(input("do you want to continue or press 0 to exit:"))
