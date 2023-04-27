def circle(r):
    return (3.14*r*r)
def cylinder(r,h):
    return ((3.14*r*r)+(2*3.14*r*h))
r=int(input("Enter radius of circle   : "))
h=int(input("Enter height of cylinder : "))
print("Area of Circle is",circle(r))
print("Surface Area of Cylinder is",cylinder(r,h))