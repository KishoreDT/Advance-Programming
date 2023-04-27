x=("apple", "banana", "cherry")
y=list(x)
n=str(input("Enter a name :"))
y.append(n)
x=tuple(y)
print("The tuple is",x)
a,b=(1,2,3),(4,5,6)
t=a+b
print("",t)