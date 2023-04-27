#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n,x;
    vector<int> ivec;
    cout<<"Enter total no. of numbers :";
    cin>>x;
    cout<<"Enter the numbers :"<<endl;
    for(int i=1;i<=x;i++)
    {
        cin>>n;
        ivec.push_back(n);
    }
    sort(ivec.begin(),ivec.end());
    vector<int>::iterator it;
    for(it=ivec.begin();it<ivec.end();it++)
    {
        cout<<*it<<" ";
    }
    return 0;
}