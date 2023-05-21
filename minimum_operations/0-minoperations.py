#!/usr/bin/python3
""" Minimum Operations """

import math

def minOperations(n):
    if n == 1:
        return 0

    # Find the factors of n
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    if not factors:
        return n

    # Initialize an array to store the minimum number of operations
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for factor in factors:
        # Copy All and Paste operation
        dp[factor] = 2

        # Check if the current factor can be further reduced
        for i in range(2, int(math.sqrt(factor)) + 1):
            if factor % i == 0:
                dp[factor] = min(dp[factor], dp[i] + dp[factor // i])

    return dp[n]

# Example usage:
n = 9
min_ops = minOperations(n)
print(f"Minimum number of operations for n = {n}: {min_ops}")
