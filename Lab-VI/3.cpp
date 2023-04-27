#include <iostream>
#include <array>
using namespace std;

int main()
{
    array<int,5> arr1={1,2,3,4,5};
    array<int,5> arr2={5,4,3,2,1};
    cout<<"The size of array is "<<arr1.size()<<endl;
    cout<<"The 1st number is "<<arr1.front()<<endl;
    cout<<"The last number is "<<arr1.back()<<endl;
    cout<<"The number at 2nd position is "<<arr1.at(2)<<endl;
    cout<<"Swapping arrays :"<<endl;
    arr1.swap(arr2);
    cout << "Output of begin and end: ";
    for (auto i = arr1.begin(); i != arr1.end(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of cbegin and cend: ";
    for (auto i = arr1.cbegin(); i != arr1.cend(); ++i)
        cout << *i << " ";
  
    cout << "\nOutput of rbegin and rend: ";
    for (auto ir = arr1.rbegin(); ir != arr1.rend(); ++ir)
        cout << *ir << " ";
  
    cout << "\nOutput of crbegin and crend : ";
    for (auto ir = arr1.crbegin(); ir != arr1.crend(); ++ir)
        cout << *ir << " ";
    return 0;
}