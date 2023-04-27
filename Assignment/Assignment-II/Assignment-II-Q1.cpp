#include <iostream>
#include <list>
#include <iterator>
using namespace std;

void showlist(list <int> g)
{
    list <int> :: iterator it;
    for(it =g.begin(); it !=g.end(); ++it)
        cout<<'\t'<<*it;
    cout<<'\n';
}

int main()
{
    int n,x;
    list<int> L1, L2;
    cout<<"Enter lenght of 1st list :";
    cin>>n;
    cout<<"Enter the numbers :"<<endl;
    for(int i=1;i<=n;i++)
    {
        cin>>x;
        L1.push_back(x);
    }
    cout<<"Enter lenght of 2nd list :";
    cin>>n;
    cout<<"Enter the numbers :"<<endl;
    for(int i=1;i<=n;i++)
    {
        cin>>x;
        L2.push_back(x);
    }
    cout<<"\nThe 1st list elements are :"<<endl;
    showlist(L1);
    cout<<"\nThe 2nd list elements are :"<<endl;
    showlist(L2);
    cout<<"\nThe reverse of 1st list is :"<<endl;
    L1.reverse();
    showlist(L1);
    cout<<"\nThe sorted list 2 :"<<endl;
    L2.sort();
    showlist(L2);
    cout<<"\nAfter removing front and back element in list 1 :"<<endl;
    L1.pop_front();
    L1.pop_back();
    showlist(L1);
    cout<<"\nAfter adding front and back elements in list 1 to list 2 :"<<endl;
    L2.push_front(L1.front());
    L2.push_back(L1.back());
    showlist(L2);
    return 0;
}