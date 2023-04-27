#include <iostream>
using namespace std;

class Line
{
    private:
        int length;
    public:
        int getter()
        {
            return length;
        }
        void setter(int l)
        {
            length=l;
        }
};
int main()
{
    Line l;
    l.setter(50);
    cout<<l.getter();
    return 0;
}