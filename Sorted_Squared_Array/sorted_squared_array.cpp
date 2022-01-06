#include <iostream>
#include <cstdlib> // for abs
#include <vector>

using namespace std;

// {-7, -5, -4, 3, 6, 8, 9}

vector<int> sortedSquaredArray(vector<int> array) {
    vector<int> sorted_array(array.size(), 0);
    
    auto left_pointer = array.begin();
    //end() points to somewhere past the end of the container. By convention, sequences in C++ are of the form [begin, end), that is, the end is not part of the sequence
    auto right_pointer = array.end() - 1;
    
    for( auto rit = sorted_array.rbegin(); rit != sorted_array.rend(); rit++)
    {
        if( abs(*left_pointer) > abs(*right_pointer))
        {
           *rit = (*left_pointer) * (*left_pointer);
           left_pointer++;
        } 
        else {
            *rit  = (*right_pointer) * (*right_pointer);
            right_pointer--;
        }
    }

	return sorted_array;
}

int main()
{
    vector<int> array {-7, -5, -4, 3, 6, 8, 9};
    vector<int> sorted_array = sortedSquaredArray(array);
    for(auto elem : sorted_array)
    {
        cout<<elem<<" ";
    }
}