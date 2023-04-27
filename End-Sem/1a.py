def menu_ordered(food):
    if food=='':
        print("I am not eating today")
    else:
        print("Today, I am eating",food)
food=input("Enter your item :")
menu_ordered(food)