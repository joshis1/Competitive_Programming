# Given two non-empty arrays of integers, write a function that determines whether the second 
# array is a subsequence of the first one. A subsequence of an array is a set of numbers that aren't 
# necessarily adjacent in the array but that are in the same order as they appear in the array. 
# For instance, the numbers [1,3,4] form a subsequence of the array [1,2,3,4], and dos do the numbers
# [2,4]. Note that a single number in an array and the array itself are both valid subsequence of the array.

# Sample Input  array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# Sample output true 


def isValidSubsequence(array, sequence):
    array_index = 0
    sequence_index = 0

    while array_index < len(array) and sequence_index < len(sequence):
        if array[array_index] == sequence[sequence_index]:
            sequence_index += 1
        array_index += 1
    
    print(len(sequence))
    print(sequence_index)
    return len(sequence) == sequence_index
         
    



if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))
