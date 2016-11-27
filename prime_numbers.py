"""
Question 1 - Primes
Write a function to determine whether a given number is prime or not (divisible only by itself and 1).
"""

__author__ = 'Stan'


def is_prime_num(number):
    # Adding a quick sanitizing on the input

    # If input number less than 2 it is not a prime, then return False
    if number < 2:
        return False
    # If input number is 2 it is prime, then return True
    elif number == 2:
        return True
    # If input number is even, then not prime, return False
    elif number % 2 == 0:
        return False
    # Speeding up the check excluding all even numbers
    # Also need to check range up to square root from input number +1
    else:
        limit = number**0.5 + 1
        i = 3
        while i <= limit:
            if number % i == 0:
                return False
            i += 2
        return True