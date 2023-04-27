#include <iostream>
#include <array>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cout<<"Enter total no. of numbers :";
    cin>>n;
    array<int,5> arr;
    cout<<"Enter the numbers :"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=0; i<(n-1); i++)
    {
        for(int j=0; j<(n-i-1); j++)
        {
            if(arr[j]>arr[j+1])
            {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    cout<<"Sorted Array :"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    array<int,5> array;
    copy(begin(arr), end(arr)-1, begin(array));
    cout<<"\nNew Array :"<<endl;
    for(int i=0;i<n-1;i++)
    {
        cout<<array[i]<<" ";
    }
}
