class A {
  public:
    void display1() {
        cout << "Inside A." ;
    }
};

class B {
    public:
    void display1() {
        cout << "Inside B" ;
    }
};

class C: public A,B {
    
};

int main() {
  C myObj;
  return 0;
}