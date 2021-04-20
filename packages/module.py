def unique(l):
    l1=[]
    for i in l:
        if l.count(i)==1:
            l1.append(i)
    print(l1)

def sd(l):
    g=[]
    for i in l:
        if(i in g):
            continue
        else:
            g.append(i)
    print(g)
    
def swap (a,b):
    temp=0
    temp=a
    a=b
    b=temp
    print("the swap value is",a,b)