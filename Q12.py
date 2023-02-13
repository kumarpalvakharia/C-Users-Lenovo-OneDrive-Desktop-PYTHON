import math
def cricle(x0,y0,r,x,y):
    z=math.sqrt((pow((x-x0),2))+(pow((y-y0),2)))
    if(z==r):
        print("Point lies on the cricle")
    elif(z>r):
        print("Point lies outside the cricle")
    else:
        print("Point lies inside the cricle")
a=int(input("Enter x0 - "))
b=int(input("Enter y0 - "))
c=int(input("Enter r - "))
d=int(input("Enter x - "))
e=int(input("Enter y - "))
cricle(a,b,c,d,e)

