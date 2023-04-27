n=int(input("Enter a number : "))
sum=0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit
   temp //= 10
print("The sum of digits :",sum)