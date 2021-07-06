'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
def primes(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
sum = 0
for i in range(2, 2000000):
    if primes(i):
        sum += i
print(sum)        

