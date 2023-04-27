#include <iostream>
using namespace std;

class Circle
{
    private:
        double x,y,r;
        static int number_of_circles;
    public:
        static void update_number_of_circles()
        {
            number_of_circles = 10;
        }
        Circle(double xaxis,double yaxis,double radius)
        {
            x=xaxis;
            y=yaxis;
            r=radius;
            update_number_of_circles();
        }
        Circle(Circle &obj)
        {
            x=obj.x;
            y=obj.y;
            r=obj.r;
            update_number_of_circles();
        }
        void display()
        {
            cout<<"Center of the Circle : ("<<x<<" , "<<y<<") Radius of the Circle : "<<r<<endl;
            cout<<"Number of circles = " << number_of_circles<<endl;
        }
        friend void updateCircle(Circle &obj);
};

void updateCircle(Circle &obj)
{
    obj.x=1.0;
    obj.y=2.0;
    obj.r=4.0;
}

int Circle::number_of_circles=0;

int main()
{
    Circle c(1.0, 2.0, 3.0);
    c.display();
    updateCircle(c);
    c.display();
    return 0;
}