#include<iostream>
#include<vector>
using spacename std;

int main()
{
    vector<int> myarray;    
}

void sort(vector<int> & array)
{
    //array.size()/2
}

int getMaxIndex(vector<int> & array,int start, int end)
{
    int max=*(array.begin());
    int ret=0;
    for(vector<int>::iterator i=array.begin()+start; i <array.begin()+end;++i)
    {
        if (*i>max)
        {
            max=*i;
            ret=i-array.begin();
        }
    }
    return ret;
}
       
    
