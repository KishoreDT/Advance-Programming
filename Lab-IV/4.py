hogwarts={
    'Wandmaker':['Geraint Olivander','Mykew Gregorovitch','Salazar Slytherin'],#Using list for Wandmaker because it is easy to add elemments
    'Teacher':['Severus Snape','Albus Dumbledore','Minerva McGonnagall'],#Using list for Teacher because it is easy to add elemments
    'House':{'Gryffindor','Slytherin','Hufflepuff','Ravenclaw'},#Using set for House because it has only 4 elemments
    'Graduate':7,
    'Subject':['Defence against the Dark Arts','Divination','History of Magic','Muggle studies']}#Using list for Wandmaker because it is easy to add elemments
l=sorted(hogwarts['Teacher'])
print(l)
hogwarts['Subject'].append('Herbology')
print(hogwarts['Subject'])
hogwarts['Wandmaker'].pop()
print(hogwarts['Wandmaker'])
n=int(input("\nEnter a number of years to graduate out of Hogwarts school :"))
hogwarts['Graduate']=n
print("Graduate :",hogwarts['Graduate'])