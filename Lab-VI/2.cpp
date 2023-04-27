#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n,x;
    vector<int> v;
    cout<<"Enter total no. of numbers :";
    cin>>x;
    cout<<"Enter the numbers :"<<endl;
    for(int i=1;i<=x;i++)
    {
        cin>>n;
        v.push_back(n);
    }
    sort(v.begin(),v.end());
    vector<int>::iterator it;
    cout<<"The vector elements are ";
    for(it=v.begin();it<v.end();it++)
    {
        cout<<*it<<" ";
    }
    cout<<"\n\nThe size of vector is "<<v.size()<<endl;
    cout<<"The capacity is "<<v.capacity()<<endl;
    cout<<"The 1st number is "<<v.front()<<endl;
    cout<<"The last number is "<<v.back()<<endl;
    cout<<"The number at 2nd position is "<<v.at(2)<<endl;
    //cout<<v.data()[0]<<endl;
    int* a=v.data();
    cout << "The vector elements are: ";
    for (int i=0;i<v.size();++i)
    {
        cout<<*a++<<" ";
    }
    v.pop_back();
    cout<<"\n\nThe new size of vector is "<<v.size()<<endl;
    cout<<"The new capacity is "<<v.capacity()<<endl;
    cout<<"The new 1st number is "<<v.front()<<endl;
    cout<<"The new last number is "<<v.back()<<endl;
    int* b=v.data();
    cout << "The new vector elements are: ";
    for (int j=0;j<v.size();++j)
    {
        cout<<*b++<<" ";
    }

    cout << "\n\nOutput of begin and end: ";
    for (auto i = v.begin(); i != v.end(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of cbegin and cend: ";
    for (auto i = v.cbegin(); i != v.cend(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of rbegin and rend: ";
    for (auto ir = v.rbegin(); ir != v.rend(); ++ir)
        cout << *ir << " ";
  
    cout << "\nOutput of crbegin and crend : ";
    for (auto ir = v.crbegin(); ir != v.crend(); ++ir)
        cout << *ir << " ";
    return 0;
}