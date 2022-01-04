#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> sortedSquaredArray(vector<int> array) {
   
   transform(array.begin(), array.end(), array.begin(), [](int elem) -> int { return elem * elem; });
   sort(array.begin(), array.end());
   return array;
}

int main()
{
    vector<int> array {1, 2, 3, 5, 6, 8, 9};
    vector<int> sorted_array = sortedSquaredArray(array);
    for(auto elem : sorted_array)
    {
        cout<<elem<<" ";
    }
}