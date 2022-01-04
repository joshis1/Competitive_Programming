
def sortedSquaredArray(array):
    # Write your code here.
    mp1 =  list(map(lambda num: num **2, array))
    return sorted(mp1)



if __name__ == "__main__":
    array = [1,2,3,5,6,8,9]
    print(sortedSquaredArray(array))

