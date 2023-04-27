class Consultation:
    def __init__(self)->None:
        p=[]
        self.p=p
    def insert(self):
        n=input("Enter Patient Name :")
        a=input("Enter Patient Age :")
        s=[n,a]
        self.p.append(s)
    def remove(self):
        self.p.pop(0)
    def display(self):
        print(self.p)
class Patient(Consultation):
    def sort(self):
        self.p.sort()
    def display(self):
        print(self.p)
c=Consultation()
p=Patient()
def run():
    print("\n1. Insert new Patient")
    print("2. Remove 1st Patient")
    print("3. Sorting the list")
    print("4. Display")
    ch=int(input("Enter your choise :"))
    if ch==1:
        c.insert()
        run()
    elif ch==2:
        c.remove()
        run()
    elif ch==3:
        p.sort()
        run()
    elif ch==4:
        c.display()
        p.display()
        run()
run()