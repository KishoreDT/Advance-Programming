l1,l2=[1,2,3],[4,5,6]
s=[[a, b] for a in l1 for b in l2 if a != b]
print("The set elements are :",s)