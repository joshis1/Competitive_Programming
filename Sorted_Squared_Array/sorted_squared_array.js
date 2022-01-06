function sortedSquaredArray(array) {
    let squared_array = new Array(array.length).fill(0);
    let left_pointer = 0;
    let right_pointer = array.length -1;

    for(index = array.length -1; index >= 0 ; index --)
    {
        if ( Math.abs(array[left_pointer]) > Math.abs(array[right_pointer]) )
        {
            squared_array[index] = array[left_pointer] * array[left_pointer];
            left_pointer += 1;
        }
        else 
        {
            squared_array[index] = array[right_pointer] * array[right_pointer];
            right_pointer -= 1;
        }
    }

    return squared_array;
   
   }
 //"array": [-2, -1]
 array = [-7, -5, -4, 3, 6, 8, 9];
 console.log(sortedSquaredArray(array));