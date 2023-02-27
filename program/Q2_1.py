import random
L=[]
x=0
M=[]
y=0
while(x!=4):
    a=random.randint(1,100)
    if a%2==0:
        L.append(a)
        x=x+1
while(y!=5):
    b=random.randint(1,100)
    if b%2!=0:
        M.append(b)
        y=y+1
print("The even list is", str(L) ,"and the odd list is ",str(M))
print("Replace the third element of odd integers with  a list of 4 even integers , and the new list is - ")
M[2]=L
print(str(M))
X=[]
for item in M:
    if isinstance(item, list):
        X.extend(item)
    else:
        X.append(item)
print("After Flattern the list is ",str(X))
print("After sorting the list is",sorted(X))

      