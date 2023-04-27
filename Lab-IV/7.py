dd={'MO':'Monday','TU':'Tuesday','WE':'Wednesday','TH':'Thursday','FR':'Friday','SA':'Saturday','SU':'Sunday'}
print("Before change :\n",dd)
dd = {v: k for k, v in dd.items()}
print("After change :\n",dd)