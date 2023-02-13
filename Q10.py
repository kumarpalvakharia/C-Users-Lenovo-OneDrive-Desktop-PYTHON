def panda(x,y):
    a=x*y
    p=2*(x+y)
    if (a>p):
        print("Area is greater than perimeter")
    else:
        print("Perimeter is greater than area")
a=int(input("Enter length- "))
b=int(input("Enter breadth- "))
panda(a,b)
