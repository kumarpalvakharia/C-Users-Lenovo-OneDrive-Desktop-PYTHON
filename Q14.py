def result(a,b,c):
    if(a<=39 or b<=39 or c<=39):
        print("FAIL")
        exit()
    else:
        print("PASS")
        t=a+b+c
        print("Total marks are ",t)
        avg=(a+b+c)/3
        print("Average Marks are ",avg)
        print("The Overall Grade Is ")
        if(avg>=40 and avg<=44):
            print("P")
        elif(avg>=45 and avg<=49):
            print("C")
        elif(avg>=50 and avg<=54):
            print("B")
        elif(avg>=55 and avg<=59):
            print("B+")
        elif(avg>=60 and avg<=69):
            print("A")
        elif(avg>= 70 and avg<=79):
            print("A+")
        elif(avg>=80 and avg<=100):
            print("O")
        else:
            print("Input Error")
x=float(input("Enter Marks of Math- "))
y=float(input("Enter Marks of Chemistry- "))
z=float(input("Enter Marks of Physics- "))
result(x,y,z)


        
