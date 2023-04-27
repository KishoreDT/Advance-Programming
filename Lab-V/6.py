def lis(l):
    l.split()
    print(l)

l=[1,2,[2,5,3],{1:"A",2:"B"}]
li=[]
for it in l:
    if type(it)==int:
        li.append(it)
print(li)