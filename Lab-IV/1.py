date=int(input("Enter Date :"))
month=int(input("Enter Month :"))
year=int(input("Enter Year :"))
day=input("Enter Day :")
dd={'MO':'Monday','TU':'Tuesday','WE':'Wednesday','TH':'Thursday','FR':'Friday','SA':'Saturday','SU':'Sunday'}
md={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
print(dd[day],',',md[month],date,',',year)