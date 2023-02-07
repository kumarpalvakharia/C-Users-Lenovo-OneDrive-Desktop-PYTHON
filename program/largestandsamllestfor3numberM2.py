def game(a,b,c):
    l=a
    if(b>a):
        l=b
    if(c>a):
        l=c
    s=a
    if(b<a):
        s=b
    if(c<a):
        s=c
    
    if(l>s):
        print("The largest number is",l,"And the smallest is",s)
    else:
        print("All are same")
x=int(input("Enter 1st number"))
y=int(input("Enter 1st number"))
z=int(input("Enter 1st number"))
game(x,y,z)
