class A:
    def display1():
        print("Inside A")
class B:
    def display2():
        print("Inside B")
class C(A,B):
    print(A.display1())
    print(B.display2())
c=C()