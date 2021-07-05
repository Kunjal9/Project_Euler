#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sum_of_sqr():
    sum = 0
    j = 1
    for i in range(1,101):
        j = i * i
        sum = sum + j
    return(sum)

def sqr_of_sum():
    sum1 = 0
    for i in range(1,101):
        sum1 = sum1 + i
        
    return(sum1*sum1)           

print(sqr_of_sum()- sum_of_sqr())