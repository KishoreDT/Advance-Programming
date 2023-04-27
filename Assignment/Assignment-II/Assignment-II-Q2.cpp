#include <iostream>
#include <vector>
#include <iterator>
using namespace std;

void showvector(vector <int> g)
{
    vector <int> :: iterator it;
    for(it =g.begin(); it !=g.end(); ++it)
        cout<<'\t'<<*it;
    cout<<'\n';
}

int main()
{
    vector<int> v;
    cout<<"The elements in the vector are :"<<endl;
    v.assign(10, 100);
    showvector(v);
    cout<<"Inserting element in the 5th position :"<<endl;
    v.insert(v.begin()+4,10);
    showvector(v);
    cout<<"Removing all the elements in the vector :"<<endl;
    v.clear();
    showvector(v);
    return 0;
}