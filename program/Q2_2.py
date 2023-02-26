import random
L=[]
for i in range(20):
    L.append(random.randint(1,100))
print("The list is - ")
print("Position  Value")
for k in range(20):
    print(k+1,"  ",L[k])
x=int(input("Enter a number from 1 to 100 - "))
print("If the number ",x," is present in the list, then the position is")
for j in range(20):
    if x==L[j]:
        print(j+1,end=",")