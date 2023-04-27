l=[1,2,3,4,5,6,7,8,9,10]
l1,l2=[],[]
for i in range(0,len(l)):
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print("The list contains odd elements :",l1)
print("The list contains even elements :",l2)
