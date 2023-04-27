org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org.extend(org)
print("\033[1ma)\033[0m","Extended org :",org,"\n   Extended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org.extend(cpy)
print("\033[1mb)\033[0m","Extended org :",org,"\n   Extended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org.append(org)
print("\033[1mc)\033[0m","Appended org :",org,"\n   Appended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org.append(cpy)
print("\033[1md)\033[0m","Appended org :",org,"\n   Appended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org.extend([4,5,6])
print("\033[1me)\033[0m","Extended org :",org,"\n   Extended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
cpy.extend([4,5,6])
print("\033[1mf)\033[0m","Extended org :",org,"\n   Extended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org.append([4,5,6])
print("\033[1mg)\033[0m","Appended org :",org,"\n   Appended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
cpy.append([4,5,6])
print("\033[1mh)\033[0m","Appended org :",org,"\n   Appended cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
org=org[0:2]
print("\033[1mi)\033[0m","Sliced org :",org,"\n   Sliced cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
cpy=cpy[0:2]
print("\033[1mj)\033[0m","Sliced org :",org,"\n   Sliced cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org=cpy[0:2]
print("\033[1mk)\033[0m","Sliced org :",org,"\n   Sliced cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
cpy=org[0:2]
print("\033[1ml)\033[0m","Sliced org :",org,"\n   Sliced cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org=org+cpy
print("\033[1mm)\033[0m","Concatenated org :",org,"\n   Concatenated cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
cpy=org+cpy
print("\033[1mn)\033[0m","Concatenated org :",org,"\n   Concatenated cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
org=org+[4,5,6]
print("\033[1mo)\033[0m","Concatenated org :",org,"\n   Concatenated cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")
org=[1,2]
cpy=org
print("Orginal list of org :",org,"\nOrginal list of cpy :",cpy,"\nID of org :", id(org),"\nID of cpy :",id(cpy),"\n")
cpy=org+[4,5,6]
print("\033[1mp)\033[0m","Concatenated org :",org,"\n   Concatenated cpy :",cpy,"\n   ID of org :", id(org),"\n   ID of cpy :",id(cpy),"\n")