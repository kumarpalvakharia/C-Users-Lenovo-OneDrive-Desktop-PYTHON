def divby10(n):
    if(n%10==0):
        return True
    else:
        return False

x=int(input("Enter the number to check it's divisiblity by 10 - "))
print(x,"is divisible by 10" if (divby10(x)) else "is not divisible by 10")
