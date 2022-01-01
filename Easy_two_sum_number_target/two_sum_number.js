function twoNumberSum(array, targetSum) {
    // Write your code here.
    matchTable = {};

    for(const num of array)
    {
        const matchNumber = targetSum - num;
       
        if( matchNumber in matchTable)
        {
            return [matchNumber, num];
        }
        else 
        {
            matchTable[num] = true;
        }

    }

    return [];
  }

  array = [3, 5, -4, 8, 11, 1, -1, 6];
  targetSum = 10;

  console.log(twoNumberSum(array, targetSum));
  
 
 