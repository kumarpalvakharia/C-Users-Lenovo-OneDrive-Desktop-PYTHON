L=[65,23,100,48,37]
print("The list of temperature in fahrenheit is ",str(L))
for i in range(5):
    L[i]=round((L[i]-32)*(5/9),2)
print("The list of temperature in celsius is",str(L))