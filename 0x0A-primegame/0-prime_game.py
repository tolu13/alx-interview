#!/usr/bin/python3

""" Prime Game Algorithm Python """


def isWinner(x, nums):
    max_n = max(nums)  # Determine the maximum n we need to consider
    if max_n < 2:
        return None  # If max_n is less than 2, there's no valid game to play

    # Step 1: Use Sieve of Eratosthenes to find all prime numbers up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while (p * p <= max_n):
        if (is_prime[p] == True):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1

    # Step 2: Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_left = sum(is_prime[1:n+1])  # Count how many primes are thr 1-9

        # Determine who wins in this game with n
        if primes_left % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    # Step 3: Decide overall winner based on the number of rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
