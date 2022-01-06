def sortedSquaredArray(array):
    sorted_array = [0 for _ in array]
    left_index = 0
    right_index = len(array) - 1

    for idx in reversed(range(len(sorted_array))):
        if abs(array[left_index]) > abs(array[right_index]):
            sorted_array[idx] = array[left_index] * array[left_index]
            left_index += 1
        else:
            sorted_array[idx] = array[right_index] * array[right_index]
            right_index -= 1
    
    return sorted_array


if __name__ == "__main__":
    array = [-7, -5, -4, 3, 6, 8, 9]
    print(sortedSquaredArray(array))
