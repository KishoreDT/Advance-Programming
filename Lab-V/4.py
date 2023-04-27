def d(n):
	if n/10 == 0:
		return 1
	return 1 + d(n // 10)
n = int(input("Enter a number : "))
print("Number of digits :",d(n)-1)