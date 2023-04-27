#include <iostream>
using namespace std;

class Sum
{
    private:
        int x,y,sum;
    public:
        Sum()
        {
            x=x;
            y=y;
            sum=sum;
        }
        void add(int x,int y)
        {
            sum=x+y;
        }
        Sum(Sum &obj)
        {
            sum=obj.sum;
        }
        friend int display(Sum);
        ~Sum()
        {
            x=0;
            y=0;
            sum=0;
        }
};

int display(Sum s)
{
    return s.sum;
}

int main()
{
    int a,b;
    cout<<"Enter 1st number : ";
    cin>>a;
    cout<<"Enter 2nd number : ";
    cin>>b;
    Sum s;
    s.add(a,b);
    cout<<"Sum : "<<display(s)<<endl;
    Sum s1;
    s1.~Sum();
    cout<<"Sum : "<<display(s1);
}