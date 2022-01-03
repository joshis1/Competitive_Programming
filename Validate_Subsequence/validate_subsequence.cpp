/* Given two non-empty arrays of integers, write a function that determines whether the second 
array is a subsequence of the first one. A subsequence of an array is a set of numbers that aren't 
necessarily adjacent in the array but that are in the same order as they appear in the array. 
For instance, the numbers [1,3,4] form a subsequence of the array [1,2,3,4], and dos do the numbers
[2,4]. Note that a single number in an array and the array itself are both valid subsequence of the array.

Sample Input  array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Sample output true 
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence)
{
    // Write your code here.
    int current_index = 0;
    int previous_index = -1;
    int search_index = 0;
    for (auto val : sequence)
    {
        auto it = find(array.begin() + search_index, array.end(), val);

        if (it != array.end())
        {
            current_index = it - array.begin();
            if (current_index <= previous_index)
            {
                return false;
            }
            previous_index = current_index;
            search_index = current_index + 1;
        }
        else
        {
            return false;
        }
    }

    return true;
}

int main()
{
    vector<int> sampleInput{5, 1, 22, 25, 6, -2, 8, 10};
    vector<int> sequence{1, 6, -1, 10};

    cout << isValidSubsequence(sampleInput, sequence);

    return 0;
}
