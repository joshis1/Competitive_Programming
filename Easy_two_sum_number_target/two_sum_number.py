def twoNumberSum(array, targetSum):
    matchTable = {}
    for num in array:
        if(targetSum - num in matchTable):
            return [num, targetSum-num]
        else:
            matchTable[num] = True
    return []

if __name__ == '__main__':
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum));