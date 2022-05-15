def nonConstructibleChange(coins):
    # o(log n) - sorting
    coins.sort() # O(log n)
    max_amount = sum(coins)
    num = None
    #print(coins)
    #print(max_amount)
    # range is [start, end)
    if len(coins) == 0:
        return 1

    for change in range(1, max_amount+1):
        if change == 1:
            if 1 not in coins:
                return 1 
        else:
            max_limit = change        
            while max_limit not in coins and max_limit != -1:
                max_limit -=1
            right_index = coins.index(max_limit)
            while 1:
                try:
            
                    # the last index is not included therefore len(coins)
                    right_index = coins.index(max_limit, right_index +1 , len(coins))
                except ValueError:
                    # print(f'final right_index = {right_index}')
                    break 
        
            print(f'right_index = {right_index}')
            print(f'change = {change}')
            print(f'max_limit = {max_limit}')
            
            num = change
            for idx in reversed(range(right_index + 1)):
                if coins[idx] > num:
                    #print(f'coins[idx] = {coins[idx]} and num = {num}')
                    continue
                #print(f'idx = {idx}')
                num = num - coins[idx]
                #print(f'num = {num}')
                if (num in coins[0:idx-1] or num == 0) and idx != 0:
                    #print(f'Setting num = {num}')
                    num = 0
                    break

            if num != 0:
                return change

    return max_amount + 1
        

                
                

if __name__ == '__main__':
   coins = [5, 7, 1, 1, 2, 3, 22]
   #coins = [1, 1, 1, 1, 1]
   print(nonConstructibleChange(coins))