d1={1:'One',2:'Two',3:'Three'}
d2={1:'One',2:'Two',3:'3'}
diff_d1_d2={}
uk=set(d1.keys())|set(d2.keys())
for k in uk:
    if d1[k]!=d2[k]:
        diff_d1_d2[k]=[d1[k],d2[k]]
print(diff_d1_d2)