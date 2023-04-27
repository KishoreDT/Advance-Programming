def fi(n):
    f=1
    for i in range(1,n+1):
        f = f * i
    return f
def fr(n):
    if n==0:
        return 1
    elif n == 1:
        return n
    else:
        return n*fr(n-1)
n=int(input("Enter a number : "))
print("The factorial in iteratively is ",fi(n))
print("The factorial in recursively is ",fr(n))
