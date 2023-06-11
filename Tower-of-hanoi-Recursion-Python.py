# f means from
# t means to
# v means via
def move(f,t):
    print("Move disc from {} to {}!".format(f,t))

#move("A","B")

def moveVia(f,v,t):
    move(f,v)
    move(v,t)

moveVia("A", "B", "C")

def hanoi(n, f, h, t): # n as number of disks, f as from, h as helper position, t as target
    if n==0 :
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(4,"A","B","C")

