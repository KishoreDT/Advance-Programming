#include <iostream>
#include <list>
using namespace std;

struct Youtube
{
    string ytname;
    float sub;
    Youtube(string ytn,float s)
    {
        ytname=ytn;
        sub=s;
    }
    bool operator==(const Youtube& yt)const
    {
        return this->ytname==yt.ytname;
        //return this->sub==yt.sub;
    }

};

struct YTfav
{
    list<Youtube> myfav;
    void operator+=(Youtube& yt)
    {
        myfav.push_back(yt);
    }
    void operator-=(Youtube& yt)
    {
        myfav.remove(yt);
    }
};


ostream& operator<<(ostream& stream,const Youtube& other)
{
    stream<<"Youtube Channel : "<<other.ytname<<"\nTotal Subscribers : "<<other.sub<<"M"<<endl;
    return stream;
}
ostream& operator<<(ostream& stream,const YTfav& other)
{
    for(Youtube yt:other.myfav)
    {
        stream<<yt;//<<"\nTotal Subscribers : "<<other.sub<<"M";
        
    }
    return stream;
}

int main()
{
    Youtube yt1("Alan Walker",40.2);
    Youtube yt2("eFootball",1.65);
    cout<<yt1;
    cout<<"\n-----------------------------------------------------------------------------------------\n";
    YTfav fav;
    fav+=yt1;
    cout<<fav;
    cout<<"\n-----------------------------------------------------------------------------------------\n";
    fav+=yt2;
    cout<<fav;
    cout<<"\n-----------------------------------------------------------------------------------------\n";
    fav-=yt2;
    cout<<fav;
    return 0;
}