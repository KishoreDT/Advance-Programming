import re
p=input("Enter the password :")
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,15}$"
pat = re.compile(reg)
mat = re.search(pat, p)
if mat:
    print("Password is valid.")
else:
    print("Password invalid !!")