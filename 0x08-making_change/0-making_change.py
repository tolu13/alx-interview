#!/usr/bin/python3
"""  determine the fewest number of coins needed to meet a given amount """

def makeChange(coins, total):
    """dynamic programming """
    value = 0
    coins.sort(reverse=True)
    
    
    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            value += total // coin
            total = total % coin

    return value if total == 0 else -1

if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
