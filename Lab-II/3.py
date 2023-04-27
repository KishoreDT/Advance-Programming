n=int(input("Enter a number : "))
if n%5==0 and n%7==0:
    print("The number is divisible by both 5 and 7")
elif n%5==0:
    print("The number is divisible by 5")
elif n%7==0:
    print("The number is divisible by 7")
else:
    print("The number is either divisible by 5 nor 7")