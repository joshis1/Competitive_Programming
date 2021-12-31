/** Two number sum **/


/** Write a function that takes in a non-empty array of distinct integers representing a target sum.
 * If any two number in the input array sum upto the target sum, the function should return them in an 
 * array, in any order. If no two numbers sum upto the target sum, the function should return an 
 * empty array. Note that the target sum is obtained by the the sum of two different integers in the 
 * array, you can't add a single integer to itself in order to obtain the target sum. You can 
 * assum that there will be at most one pair of numbers summing up to the target.
 * */


#include <iostream>

#include <vector>
#include <map>

using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
   map<int, int> mp;
   for(int i = 0; i< array.size(); i++)
   {
       mp.insert(std::pair<int, int>(array[i], i));
   }

   for( auto x: mp)
   {
       map<int, int>::iterator it;

       it = mp.find(targetSum - x.first);

       if( it != mp.end())
       {
           return { x.first, it->first};
       }
   }

   return {};
}

int main()
{
   vector<int> test_vector{3, 5, -4, 8, 11, 1, -1, 6};
   int target_sum = 10;

   vector<int> result = twoNumberSum(test_vector, target_sum);

   for(auto val : result)
   {
       cout<<val<<" ";
   }

}