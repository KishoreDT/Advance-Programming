#include <iostream>
using namespace std;

class Distance
{
    private:
        int feet,inches;
    public:
        Distance()
        {
            feet=0;
            inches=0;
        }
        Distance(int a,int b)
        {
            feet=a;
            inches=b;
        }
        void display()
        {
            cout<<feet<<" feet "<<inches<<" inches"<<endl;
        }
};
int main()
{
    int a,b;
    cout<<"Enter feet : ";
    cin>>a;
    cout<<"Enter inches : ";
    cin>>b;
    Distance obj;
    cout<<"Default Value : ";
    obj.display();
    Distance obj1(a,b);
    cout<<"Specfic value : ";
    obj1.display();
    return 0;
}