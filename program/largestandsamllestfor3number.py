def game(a,b,c):
    L=[]
    L.append(a)
    L.append(b)
    L.append(c)
    o=max(L)
    p=min(L)
    if(o>p):
        print("The largest number is",o)
        print("The smallest number is ",p)
    else:
        print("All are same")
x=int(input("Enter 1st number"))
y=int(input("Enter 1st number"))
z=int(input("Enter 1st number"))
game(x,y,z)
