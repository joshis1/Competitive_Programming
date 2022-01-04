/* Write a function that takes in a non-empty array of integers that are sorted in 
ascending order and returns a new array of the same length with the squares of the 
original integers also sorted in the ascending order */

function sortedSquaredArray(array) {
 
   const new_array = array.map ( val => val * val);
    new_array.sort(function(a, b) {
        return a - b;
    });
    return new_array;
  }
//"array": [-2, -1]
array = [1,2,3,5,6,8,9];
console.log(sortedSquaredArray(array));