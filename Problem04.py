'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def palindromic():
    n = 0
    for  a in range( 100,1000):
        for b in range(100,1000):
            x = str(a*b)
            if x == x[::-1] and int(x)>n:
                n = a * b
    return(n)

print(palindromic())    


