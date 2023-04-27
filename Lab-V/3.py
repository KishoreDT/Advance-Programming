def mi(L):
    max = None
    for num in L:
        if (max is None or num > max):
            max = num
    return max
def mr(L):
    length=len(L)
    if length == 1:
        return L
    elif L[length-1]>=L[length-2]:
        del L[length-2]
    elif L[length-1]<=L[length-2]:
        del L[length-1] 
    return mr(L)
L=[1,2,5,3,6,8,4,7,9,10,8]
print("Maximum is iteration is ",mi(L))
print("Maximum is rucursion is ",mr(L))
