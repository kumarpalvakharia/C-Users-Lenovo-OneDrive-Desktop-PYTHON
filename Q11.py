def slop(x1,y1,x2,y2,x3,y3):
    s1=(y2-y1)/(x2-x1)
    s2=(y3-y2)/(x3-x2)
    if (s1==s2):
        print("Points are in same line")
    else:
        print("Points are not in same line")
a=int(input("Enter x1- "))
b=int(input("Enter y1- "))
c=int(input("Enter x2- "))
d=int(input("Enter y2- "))
e=int(input("Enter x3- "))
f=int(input("Enter y3- "))
slop(a,b,c,d,e,f)