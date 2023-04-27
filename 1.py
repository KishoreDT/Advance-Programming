f=open("1.txt","w")
from itertools import combinations  
from itertools import product
seq = product(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], repeat=4)  
#seq = product(['a','d','g','h','k','i','m','n','p','r','t','u'], repeat=4)  
a="\n"
fd="170671"
sd="160109"
for p in list(seq):
    f.writelines(p)
    f.writelines(fd)
    f.writelines(a)
    f.writelines(p)
    f.writelines(sd)
    f.writelines(a)
    
f.close()