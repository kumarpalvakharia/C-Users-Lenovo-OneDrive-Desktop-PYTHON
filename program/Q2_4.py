import random
L=[]
X=[]
Y=[]
for i in range(30):
    L.append(random.randint(-100,100))
print("The whole list is - ",str(L))
for j in L:
    if j>=0:
        X.append(j)
    else:
        Y.append(j)
print("The positive portion is - ",str(X))
print("The negative portion is - ",str(Y))