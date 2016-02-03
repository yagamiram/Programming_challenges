'''
minimum number of coins to get value K
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.
Approach: Dynamic programming  (Top down without memoization)
Either pick the coin and do not pick the coin
If you pick the coin, the value decreases = min_coins(coins, low+1, high, value-coins[low])+1
If you don't pick the coin, the value remains as it is = min_coins(coins, low+1, high, value)
'''
def min_coins(coins, low, high, value):
    if len(coins) == 0 or value <= 0:
        return 0
    if low > high:
        return float('inf')
    else:
        # you can pick or u can skip a coin
        # if a coin is picked , decrement the value by the coin value
        # else leave the value as it is
        with_coin = min_coins(coins, low+1, high, value-coins[low])+1
        without_coin = min_coins(coins, low+1, high, value)
        #print with_coin, without_coin
        return min(with_coin, without_coin)
coins = [1,2,1,1,2,3,2,1,3,4,5]
print min_coins(coins, 0, len(coins)-1, 15)
