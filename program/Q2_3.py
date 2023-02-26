import random
L=[]
X=[]
for i in range(50):
    L.append(random.randint(1,30))
print("The list before removing duplicate is- ",str(L))
for j in L:
    if j not in X:
        X.append(j)
print("The list before removing duplicate is- ",str(X))
