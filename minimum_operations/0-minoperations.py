#!/usr/bin/python3
'''A function that calculates the fewest number of operations 
needed to result in exactly `n` `H` characters in a text file using 
only two operations: `Copy All` and `Paste`. '''

def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
