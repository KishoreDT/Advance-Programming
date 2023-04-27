import pandas as pd
s=input("Enter string :")
print(pd.Series(list(s)).value_counts())