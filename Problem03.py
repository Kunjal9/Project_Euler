'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import math
def max_prime_factor(n):
    while n % 2 == 0:
        max_prime = 2
        n /= 1
    for i in range(3, int(math.sqrt(n)) + 1,2):
        while n % i == 0:
            max_prime = i
            n = n/i
    if n>2:
        max_prime = n
    return int(max_prime)
print(max_prime_factor(600851475143))                
