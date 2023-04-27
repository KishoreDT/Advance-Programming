#include <iostream>
using namespace std;

struct Vector2
{
    float x,y;
    public:
    Vector2(float x,float y):x(x),y(y){}
    Vector2 add(const Vector2& other) const
    {
        return Vector2(x+other.x,y+other.y);
    }
    Vector2 operator+(const Vector2& other) const
    {
        return add(other);
    }
    Vector2 multiply(const Vector2& other)const
    {
        return Vector2(x*other.x,y*other.y);
    }
    Vector2 operator*(const Vector2& other)const
    {
        return multiply(other);
    }
};
ostream& operator<<(ostream& stream,const Vector2& other)
{
    stream<<other.x<<" , "<<other.y;\
    return stream;
}

int main()
{
    Vector2 position(2.0f,2.0f);
    Vector2 velocity(2.0f,2.0f);
    Vector2 powerup(3.0f,3.0f);
    Vector2 result=(position+velocity)*powerup;
    cout<<result<<endl;

}
