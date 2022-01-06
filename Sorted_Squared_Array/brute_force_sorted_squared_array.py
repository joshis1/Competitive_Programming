
def sortedSquaredArray(array):
    # Write your code here.
    mp1 =  list(map(lambda num: num **2, array))
    return sorted(mp1) # Time complexity O(nlogn)


if __name__ == "__main__":
    array = [-7, -5, -4, 3, 6, 8, 9]
    print(sortedSquaredArray(array))

