list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list3=[]
for ele in list1:
    if ele not in list2:
        list3.append(ele)
    else:
        pass

print(list3)